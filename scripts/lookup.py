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
    password='postgres'
)
cur = conn.cursor()

try:
    start = time.time()
    print("Start:")
    cur.execute("""
        SELECT * FROM synonyms WHERE Synonym LIKE '%dimethyl%';
        """)
    result = cur.fetchall()
    print("Matches for dimethyl on Gin table = ", len(result))
    end = time.time()
    print("Seconds it took on gin : ", (end-start))
    start = time.time()
    cur.execute("""
        SELECT * FROM synonyms_nongin WHERE Synonym LIKE '%dimethyl%';
        """)
    result = cur.fetchall()
    print("Matches for dimethyl on non Gin table = ", len(result))
    end = time.time()
    print("Seconds it took on non Gin : ", (end-start))
    start = time.time()
    cur.execute("""
        SELECT * FROM synonyms WHERE Synonym LIKE '%inner salt%';
        """)
    result = cur.fetchall()
    print("Matches for inner salt on Gin table = ", len(result))
    end = time.time()
    print("Seconds it took on Gin : ", (end-start))
    start = time.time()
    cur.execute("""
        SELECT * FROM synonyms_nongin WHERE Synonym LIKE '%inner salt%';
        """)
    result = cur.fetchall()
    print("Matches for inner salt on non Gin table ", len(result))
    end = time.time()
    print("Seconds it took on non Gin : ", (end-start))
    start = time.time()
    cur.execute("""
        SELECT * FROM synonyms WHERE Synonym LIKE '%JWAZRIHNYRIHIV-UHFFFAOYSA-N%';
        """)
    result = cur.fetchall()
    print("Matches for JWAZRIHNYRIHIV-UHFFFAOYSA-N on Gin table = %s", len(result))
    end = time.time()
    print("Seconds it took on Gin : ", (end-start))
    start = time.time()
    cur.execute("""
        SELECT * FROM synonyms_nongin WHERE Synonym LIKE '%JWAZRIHNYRIHIV-UHFFFAOYSA-N%';
        """)
    result = cur.fetchall()
    print("Matches for JWAZRIHNYRIHIV-UHFFFAOYSA-N on non Gin table = %s", len(result))
    end = time.time()
    print("Seconds it took on non Gin : ", (end-start))
    start = time.time()
    cur.execute("""
         SELECT * FROM synonyms WHERE CID = '1';
         """)
    result = cur.fetchall()
    print("Matches for CID(1) on gin table  = %s", len(result))
    end = time.time()
    print("Seconds it took on Gin : ", (end-start))
    start = time.time()
    cur.execute("""
        SELECT * FROM synonyms_nongin WHERE CID = '1';
        """)
    result = cur.fetchall()
    print("Matches for CID(1) on non gin table = %s", len(result))
    end = time.time()
    print("Seconds it took on non Gin : ", (end-start))
    cur.close()
    conn.close()
except Exception:
    traceback.print_exc()
    print("Error")
