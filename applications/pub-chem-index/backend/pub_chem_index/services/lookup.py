import psycopg2
import glob
import os
import csv
import time
import traceback

from cloudharness import applications

def connect():
    app = applications.get_configuration('pub-chem-index')
    conn_string = f"postgres://{app.db_name}:{app.harness.database.postgres.ports[0]['port']}/asu?user={app.harness.database.user}&password=metacell"
    conn = psycopg2.connect(conn_string)
    return conn

def get_all_molecules():
    conn = connect()
    cur = connect().cursor()

    try:
        cur.execute("""
            SELECT * FROM synonyms;
            """)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        traceback.print_exc()
        return 'Error submitting operation: %s' % e, 500

def search_molecules_by_synonym(term):
    conn = connect()
    cur = connect().cursor()
    try:
        cur.execute("""
            SELECT * FROM synonyms WHERE Synonym LIKE %(search)s ESCAPE '='
            """, dict(search= '%'+term+'%'))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        traceback.print_exc()
        return 'Error submitting operation: %s' % e, 500


def search_molecules_by_cid(term):
    conn = connect()
    cur = connect().cursor()
    try:
        cur.execute("""
         SELECT * FROM synonyms WHERE CID = %s;
         """,
         (term,))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        traceback.print_exc()
        return 'Error submitting operation: %s' % e, 500