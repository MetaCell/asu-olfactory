import pandas as pd
import numpy
import os
import sys
import csv
import logging
import psycopg2

from psycopg2.extensions import register_adapter, AsIs
from cloudharness import applications


def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)


register_adapter(numpy.int64, addapt_numpy_int64)

app = applications.get_configuration("pub-chem-index")
conn_string = f"postgres://{app.db_name}:{app.harness.database.postgres.ports[0]['port']}/asu?user={app.harness.database.user}&password={app.harness.database.get('pass')}"

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

NUM_PROCESSES = 2
NUM_QUEUE_ITEMS = 20

#
# WARNING!!! use head command on files for debugging
# head -n 500000 CID-SMILES > CID-SMILES-head
#

# "https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz"

added_col_dic = {
    "CID-InChI-Key": ["CID", "InChI", "Key"],
    "CID-Mass": ["CID", "Molecule", "Mass1", "Mass2"],
    "CID-PMID": ["CID", "PMID"],
    "CID-Parent": ["CID", "Parent"],
    "CID-Patent": ["CID", "Patent"],
    "CID-SID": ["CID", "SID"],
    "CID-MeSH": ["CID", "MeSH"],
    "CID-SMILES": ["CID", "SMILES"],
    "CID-Synonym-filtered": ["CID", "Synonym"],
    "CID-Synonym-unfiltered": ["CID", "Syn"],
    "CID-Title": ["CID", "Title"],
    "CID-IUPAC": ["CID", "IUPAC"],
}


def change_permissions_recursive(path, mode):
    for root, dirs, files in os.walk(path, topdown=False):
        for file in [os.path.join(root, f) for f in files]:
            if file.startswith("export-"):
                os.chmod(file, mode)
    # os.chmod(path, mode)


def create_table(conn, table_name):
    # Populate GIN indexed table, this will take about 30 minutes.
    column_names = added_col_dic[table_name]
    column_names = [x.upper() for x in column_names]
    table_name = table_name.replace("-", "_").upper()

    str_column_names = ""

    for i in column_names:
        if i != "CID":
            str_column_names += i + " VARCHAR,"

    str_column_names = str_column_names[: len(str_column_names) - 1]

    sql_drop_table = """
  DROP TABLE IF EXISTS %s
  """ % (
        table_name
    )  # better management

    sql_create_table = """
  CREATE TABLE %s (
      CID INTEGER NOT NULL,
      %s
  )
  """ % (
        table_name,
        str_column_names,
    )  # better management

    with conn.cursor() as cur:
        cur.execute(sql_drop_table)
        cur.execute(sql_create_table)

    logging.info("Table created %s ", table_name)


def bulk_insert(conn, data, file_name):
    with conn.cursor() as cur:
        table_name = file_name.replace("-", "_").upper()
        columns = added_col_dic[file_name]
        column_list = ", ".join(columns)
        records_list_template = ",".join(["%s"] * len(data))
        insert_query = "insert into {table_name} ({columns}) values {};".format(
            records_list_template, table_name=table_name, columns=column_list
        )
        cur.execute(insert_query, data)
        logging.info(f"Insert done, {len(data)} records")


def create_indexes(conn, table_name):
    with conn.cursor() as cur:
        column_names = added_col_dic[table_name]
        column_names = [x.upper() for x in column_names]
        main_column = column_names[1].lower()
        table_name = table_name.replace("-", "_").lower()

        logging.info("Create index pg_trgm")
        cur.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
        logging.info(f"Create index idx_gin_{table_name}")
        cur.execute(
            f"CREATE INDEX IF NOT EXISTS idx_gin_{table_name} ON {table_name} USING gin ({main_column} gin_trgm_ops)"
        )
        logging.info(f"Create index cid_idx_{table_name}")
        cur.execute(
            f"CREATE INDEX IF NOT EXISTS cid_idx_{table_name} ON {table_name} (CID)"
        )
        logging.info("Creating indexes done")


def get_line(file_name):
    with open(file_name) as file:
        for i in file:
            yield i


def go():
    logging.info(f"Connecting with string: {conn_string}")
    conn = psycopg2.connect(conn_string)

    path = sys.argv[1]
    logging.info("Populating table using files from %s", path)

    file_list = [path + "/" + f for f in os.listdir(path) if f.startswith("CID-")]
    for file in sorted(file_list):
        file_name = os.path.basename(file)
        column_name = ["CID", file_name]
        types = {file_name: "string", "CID": "Int64"}
        column_names = added_col_dic[file_name]
        # column_names = [x.upper() for x in column_names]
        main_column = column_names[1]  # .upper()

        if file_name in added_col_dic:
            column_name = added_col_dic[file_name]
            types = {"CID": "string"}
            for c in column_name:
                if c != "CID":
                    types[c] = "string"

        create_table(conn, file_name)

        encoding = None
        if file_name == "CID-Title":
            encoding = "Latin"
        chunksize = 1000000

        with open(file) as f:
            data = []
            for line in f:
                data.append(tuple(line.replace("\n","").split("\t")))
                if len(data) == chunksize:
                    with conn:
                        bulk_insert(conn, data, file_name)
                    data = []

        if len(data) != chunksize:
            # insert the left over data
            with conn:
                bulk_insert(conn, data, file_name)

        create_indexes(conn, file_name)


go()
