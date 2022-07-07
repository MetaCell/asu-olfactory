import psycopg2
import glob
import os
import csv
import time
import traceback

conn = psycopg2.connect(
    host='pubchem-db',
    port=5432,
    dbname='asu',
    user='mnp',
    password='metacell'
)
cur = conn.cursor()

try:
    start = time.time()
    print("Start:")
    cur.execute("""
        SELECT * FROM synonyms WHERE Synonym LIKE '%sys.argv[1]%';
        """)
    result = cur.fetchall()
    print("Matches for dimethyl on Gin table = ", len(result))
    end = time.time()
    print("Seconds it took for lookup : ", (end-start))
    cur.close()
    conn.close()
except Exception:
    traceback.print_exc()
    print("Error")
