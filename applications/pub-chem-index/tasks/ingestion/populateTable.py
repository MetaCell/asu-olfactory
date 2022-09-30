from calendar import c
import psycopg2
import glob
import os
import csv
import time
import traceback
import os
import sys
import logging

from cloudharness import applications

app = applications.get_configuration('pub-chem-index')
conn_string = f"postgres://{app.db_name}:{app.harness.database.postgres.ports[0]['port']}/asu?user={app.harness.database.user}&password=metacell"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()

added_col_dic = {
    "CID-InChI-Key": ["CID", "InChI", "Key"],
    "CID-Mass": ["CID", "Molecule", "Mass1", "Mass2"],
    "CID-PMID": ["CID", "PMID"],
    "CID-Parent": ["CID", "Parent"],
    "CID-Patent": ["CID", "Patent"],
    "CID-SID": ["CID", "SID"],
    "CID-MeSH": ["CID", "MeSH"],
    "CID-SMILES": ["CID", "SMILES"],
    "CID-Synonym-filtered": ["CID", "Syn"],
    "CID-Synonym-unfiltered": ["CID", "Syn"],
    "CID-Title": ["CID", "Title"],
    "CID-IUPAC": ["CID", "IUPAC"]
  }

try:
    #Populate a table without GIN Indexing
    start = time.time()
    # use glob to get all the csv files in the folder

    path = sys.argv[1]
    logging.info("Populating table using files from %s", path)

    file_list = [path + '/' + f for f in os.listdir(path) if f.startswith('CID-')]

    for folder in sorted(file_list):
        logging.info("Reading folder %s", folder)
        file_name = os.path.basename(folder)
        csv_files = glob.glob(os.path.join(folder, "*.csv"))

        table_name = file_name.replace('-','')
        #Populate GIN indexed table, this will take about 30 minutes.
        sql_copy = """
            CREATE TABLE IF NOT EXISTS %s(
                CID VARCHAR NOT NULL,
                %s VARCHAR
            )
            """ % (table_name, added_col_dic[file_name][1]) 

        if file_name == "CID-InChI-Key":
            sql_copy = """
            CREATE TABLE IF NOT EXISTS %s(
                CID VARCHAR NOT NULL,
                %s VARCHAR
                %s VARCHAR
            )
            """ % (table_name, added_col_dic[file_name][1],added_col_dic[file_name][2]) 
        elif file_name == "CID-Mass":
            sql_copy = """
            CREATE TABLE IF NOT EXISTS %s(
                CID VARCHAR NOT NULL,
                %s VARCHAR
                %s VARCHAR
                %s VARCHAR
            )
            """ % (table_name, added_col_dic[file_name][1],added_col_dic[file_name][2], added_col_dic[file_name][3])        
        cur.execute(sql_copy)
        logging.info("Table created %s", sql_copy)
        
        # loop over the list of csv files
        for f in csv_files:
            logging.info("Ingesting file %s", f)
            sql_copy = '''
                COPY %s
                FROM '%s'
                DELIMITER ',' CSV HEADER;
               '''  % (table_name % f)
            logging.info("Query is %s", sql_copy)
            cur.execute(sql_copy)
        cur.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
        sql_copy = '''CREATE INDEX IF NOT EXISTS idx_gin ON %s USING gin (Synonym gin_trgm_ops);''' % table_name
        cur.execute(sql_copy)
        sql_copy = '''CREATE INDEX IF NOT EXISTS cid_idx ON %s (CID);''' % table_name
        cur.execute(sql_copy)
        conn.commit()   
except Exception:
    logging.error("Error during ingestion", exc_info=True)
    exit(1)
finally:
    cur.close()
    conn.close()
    end = time.time()
    logging.info("It took %s seconds to create GIN table. ", end - start)