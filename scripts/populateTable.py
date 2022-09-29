from calendar import c
import psycopg2
import glob
import os
import csv
import time
import traceback
import os

conn = psycopg2.connect(
    host='172.17.0.2',
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
    path = '../CID_Chunks'

    file_list = [path + '/' + f for f in os.listdir(path) if f.startswith('CID-')]

    for folder in sorted(file_list):
        print(folder)
        file_name = os.path.basename(folder)
        print(file_name)
        csv_files = glob.glob(os.path.join(folder, "*.csv"))

        #Populate GIN indexed table, this will take about 30 minutes.
        start = time.time()
        sql_copy = """
            CREATE TABLE IF NOT EXISTS '%s'(
                CID VARCHAR NOT NULL,
                Synonym VARCHAR
            )
            """ % file_name 
        cur.execute(sql_copy)
            
        print(csv_files)
        # loop over the list of csv files
        for f in csv_files:
            print(f)
            sql_copy = '''
                COPY '%s'
                FROM '%s'
                DELIMITER ',' CSV HEADER;
               '''  % file_name % f
            cur.execute(sql_copy)
        cur.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
        cur.execute("CREATE INDEX idx_gin ON synonyms USING gin (Synonym gin_trgm_ops);")
        conn.commit()
        cur.close()
        conn.close()
        end = time.time()
        print("It took %s seconds to create GIN table. ", end - start)
except Exception:
    traceback.print_exc()
    print("Error")