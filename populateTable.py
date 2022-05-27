import psycopg2
import glob
import os
import csv
import time
import traceback

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='asu',
    user='postgres',
    password='password'
)
cur = conn.cursor()

try:
    start = time.time()
    print("Start:")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS synonyms(
            CID VARCHAR NOT NULL,
            Synonym VARCHAR
        )
        """)
    # use glob to get all the csv files in the folder
    path = "/home/walrus/code/metacell/asu/asu-olfactory/CID_Chunks/"
    csv_files = glob.glob(os.path.join(path, "*.csv"))
  
    # loop over the list of csv files
    for f in csv_files:
        print(f)
        sql_copy = '''
            COPY synonyms
            FROM '%s'
            DELIMITER ',' CSV HEADER;
            ''' % f
        cur.execute(sql_copy)
    cur.execute("CREATE EXTENSION pg_trgm")
    cur.execute("CREATE INDEX idx_gin ON synonyms USING gin (Synonym gin_trgm_ops);")
    conn.commit()
    cur.close()
    conn.close()
    end = time.time()
    print("End Time")
    print(end - start)
except Exception:
    traceback.print_exc()
    print("Error")