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

try:
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
    cur.execute("CREATE INDEX IF NOT EXISTS idx_gin ON synonyms USING gin (Synonym gin_trgm_ops);")
    
    
except Exception:
    logging.error("Error during ingestion", exc_info=True)
    exit(1)
finally:
    conn.commit()
    cur.close()
    conn.close()
    end = time.time()
    logging.info("It took %s seconds to create GIN table. ", end - start)