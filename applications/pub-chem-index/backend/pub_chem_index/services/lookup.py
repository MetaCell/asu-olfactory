import psycopg2
import glob
import os
import csv
import time
import traceback

def search_molecules_by_synonym(term):
    conn = psycopg2.connect(
        host='pubchem-db',
        port=5432,
        dbname='asu',
        user='mnp',
        password='metacell'
    )
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT * FROM synonyms WHERE Synonym LIKE %(term)s;
            """, (term))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        traceback.print_exc()
        return 'Error submitting operation: %s' % e, 500


def search_molecules_by_cid(term):
    conn = psycopg2.connect(
        host='pubchem-db',
        port=5432,
        dbname='asu',
        user='mnp',
        password='metacell'
    )
    cur = conn.cursor()
    try:
        cur.execute("""
         SELECT * FROM synonyms WHERE CID = %s;
         """,
         (term))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        traceback.print_exc()
        return 'Error submitting operation: %s' % e, 500