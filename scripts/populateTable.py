from calendar import c
import psycopg2
import glob
import os
import csv
import time
import traceback
import os
import logging

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='asu',
    user='postgres',
    password='postgres'
)
cur = conn.cursor()

try:
    #Populate a table without GIN Indexing
    start = time.time()
    # use glob to get all the csv files in the folder

    path = "/tmp/CID"
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
                Synonym VARCHAR
            )
            """ % table_name 
        cur.execute(sql_copy)
        logging.info("Table created")
        
        # loop over the list of csv files
        for f in csv_files:
            logging.info("Ingesting file %s", f)
            sql_copy = '''
                COPY %s
                FROM '%s'
                DELIMITER ',' CSV HEADER;
               '''  % (table_name , f)
            logging.info("Query is %s", sql_copy)
            cur.execute(sql_copy)
        cur.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
        sql_copy = '''CREATE INDEX IF NOT EXISTS idx_gin ON %s USING gin (Synonym gin_trgm_ops);''' % table_name
        cur.execute(sql_copy)
        sql_copy = '''CREATE INDEX IF NOT EXISTS cid_idx ON %s (CID);''' % table_name
        cur.execute(sql_copy)   
except Exception:
    logging.error("Error during ingestion", exc_info=True)
    exit(1)
finally:
    conn.commit()
    cur.close()
    conn.close()
    end = time.time()
    logging.info("It took %s seconds to create GIN table. ", end - start)