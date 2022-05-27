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
        SELECT * FROM synonyms_test WHERE synSynonymonym LIKE '%dimethyl%';
        """)
    result = cur.fetchall()
    print("Matches for dimethyl = %s", len(result))
    end = time.time()
    print("It took %s (mins, secs) : ", divmod(end-start,60))
    start = time.time()
    cur.execute("""
        SELECT * FROM synonyms_test WHERE Synonym LIKE '%inner salt%';
        """)
    result = cur.fetchall()
    print("Matches for inner salt = %s", len(result))
    end = time.time()
    print("It took %s (mins, secs) :", divmod(end-start,60))
    start = time.time()
    cur.execute("""
        SELECT * FROM synonyms_test WHERE Synonym LIKE '%JWAZRIHNYRIHIV-UHFFFAOYSA-N%';
        """)
    result = cur.fetchall()
    print("Matches for JWAZRIHNYRIHIV-UHFFFAOYSA-N = %s", len(result))
    end = time.time()
    print("It took %s (mins, secs) :", divmod(end-start,60))
    # cur.execute("""
    #     SELECT * FROM synonyms_test WHERE CID='1';
    #     """)
    # result = cur.fetchall()
    # print("Matches for CID(1) = %s", len(result))
    # end = time.time()
    # print("It took %s minutes", (end-start)/60)
    cur.close()
    conn.close()
except Exception:
    traceback.print_exc()
    print("Error")

