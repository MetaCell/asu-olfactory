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

conn = psycopg2.connect(
    host='pubchem-db',
    port=5432,
    dbname='asu',
    user='mnp',
    password='metacell'
)
cur = conn.cursor()

try:
    #Populate a table without GIN Indexing
    # start = time.time()
    # cur.execute("""
    #     CREATE TABLE IF NOT EXISTS synonyms_nongin(
    #         CID VARCHAR NOT NULL,
    #         Synonym VARCHAR
    #     )
    #     """)
    # # use glob to get all the csv files in the folder
    # path = '/CID_Chunks'
    # csv_files = glob.glob(os.path.join(path, "*.csv"))
    # # loop over the list of csv files
    # for f in csv_files:
    #     sql_copy = '''
    #         COPY synonyms_nongin
    #         FROM '%s'
    #         DELIMITER ',' CSV HEADER;
    #         ''' % f
    #     cur.execute(sql_copy)

    # conn.commit()
    # end = time.time()
    # print("It took %s seconds to create Non GIN table. ", end - start)
    #Populate GIN indexed table, this will take about 30 minutes.
    start = time.time()
    path = sys.argv[1]
    logging.info("Populating table using files from %s", path)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS synonyms(
            CID VARCHAR NOT NULL,
            Synonym VARCHAR
        )
        """)

    logging.info("Table created")
    # use glob to get all the csv files in the folder
    csv_files = glob.glob(os.path.join(path, "*.csv"))
    # loop over the list of csv files
    for f in csv_files:
        logging.info("Ingesting file %s", f)
        sql_copy = '''
            COPY synonyms
            FROM '%s'
            DELIMITER ',' CSV HEADER;
            ''' % f
        logging.info("Query is %s", sql_copy)
        cur.execute(sql_copy)
        logging.info("Ingesting file %s", f)
    cur.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
    cur.execute("CREATE INDEX idx_gin ON synonyms USING gin (Synonym gin_trgm_ops);")
    
    
except Exception:
    logging.error("Error during ingestion", exc_info=True)
    exit(1)
finally:
    conn.commit()
    cur.close()
    conn.close()
    end = time.time()
    logging.info("It took %s seconds to create GIN table. ", end - start)