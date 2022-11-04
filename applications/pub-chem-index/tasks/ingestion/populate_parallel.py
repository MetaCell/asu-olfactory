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
    "CID-Synonym-unfiltered": ["CID", "Synonym"],
    "CID-Title": ["CID", "Title"],
    "CID-IUPAC": ["CID", "IUPAC"],
    "CID-Component": ["CID", "component"],
}

gin_indexes_tables = ['CID-Title', 'CID-MeSH', 'CID-IUPAC', 'CID-InChI-Key', 'CID-Synonym-filtered']

def change_permissions_recursive(path, mode):
    for root, dirs, files in os.walk(path, topdown=False):
        for file in [os.path.join(root, f) for f in files]:
            if file.startswith("export-"):
                os.chmod(file, mode)
    # os.chmod(path, mode)


def execute_sql(conn, command):
    with conn.cursor() as cur:
        logging.info(f"Execute {command}")
        cur.execute(command)
        conn.commit()


def create_table(conn, table_name):
    # Populate GIN indexed table, this will take about 30 minutes.
    column_names = added_col_dic[table_name]
    column_names = [x.upper() for x in column_names]
    table_name = table_name.replace("-", "_").upper()

    str_column_names = ""
    for i in column_names:
        if i == "CID":
            str_column_names += i + " INTEGER NOT NULL,"
        else:
            str_column_names += i + " VARCHAR,"

    str_column_names = str_column_names[: len(str_column_names) - 1]

    sql_drop_table = f"DROP TABLE IF EXISTS {table_name}"
    sql_create_table = f"CREATE TABLE {table_name} ({str_column_names})"

    execute_sql(conn, sql_drop_table)
    execute_sql(conn, sql_create_table)

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
        conn.commit()


def create_indexes(conn, table_name, create_gin):
    column_names = added_col_dic[table_name]
    column_names = [x.upper() for x in column_names]
    main_column = column_names[1].lower()
    table_name = table_name.replace("-", "_").lower()


    if create_gin:
        logging.info("Start creating indexes")
        execute_sql(conn, "CREATE EXTENSION IF NOT EXISTS pg_trgm;")
        execute_sql(conn, f"CREATE INDEX IF NOT EXISTS idx_gin_{table_name} ON {table_name} USING gin ({main_column} gin_trgm_ops);")
        execute_sql(conn, f"CREATE INDEX IF NOT EXISTS cid_idx_{table_name} ON {table_name} (CID);")
        logging.info("Finish creating indexes")


def get_line(file_name):
    with open(file_name) as file:
        for i in file:
            yield i


def go():
    logging.info(f"Connecting with string: {conn_string}")
    conn = psycopg2.connect(conn_string)

    file = sys.argv[1]
    file_name = os.path.basename(file)
    logging.info(f"Populating table using file {file_name}")

    column_name = ["CID", file_name]
    types = {file_name: "string", "CID": "Int64"}
    column_names = added_col_dic[file_name]
    # column_names = [x.upper() for x in column_names]
    main_column = column_names[1]  # .upper()
    gin_indexed = file_name in gin_indexes_tables

    if file_name in added_col_dic:
        column_name = added_col_dic[file_name]
        types = {"CID": "string"}
        for c in column_name:
            if c != "CID":
                types[c] = "string"

    create_table(conn, file_name)

    encoding = "UTF-8"
    if file_name == "CID-Title":
        encoding = "Latin"
    chunksize = 200000
    column_slice_size = len(column_names)

    logging.info("Inserting...")
    record_counter = 0
    with open(file, "rb") as f:
        data = []
        for line in f:
            data.append(tuple(line.decode(encoding).replace("\n","").split("\t")[:column_slice_size]))
            if len(data) == chunksize:
                with conn:
                    bulk_insert(conn, data, file_name)
                    record_counter += chunksize
                    if record_counter%5000000 == 0:
                        logging.info(f"Total number of records inserted: {record_counter}")
                data = []

    # insert the left over data (if there is any)
    if len(data) != chunksize:
        with conn:
            bulk_insert(conn, data, file_name)
            record_counter += len(data)
            logging.info(f"Total number of records inserted: {record_counter}")
    logging.info("Inserting done...")

    create_indexes(conn, file_name, gin_indexed)


go()
