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

def get_all_values(table_name):
    conn = connect()
    cur = connect().cursor()

    try:
        cur.execute("""
            SELECT * FROM %s;
            """, table_name)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        traceback.print_exc()
        return 'Error submitting operation: %s' % e, 500

def search_table_by_value(table_name, key, term):
    conn = connect()
    cur = connect().cursor()
    try:
        cur.execute("""
            SELECT * FROM %s WHERE %s LIKE %(search)s ESCAPE '='
            """, ( table_name, key, dict(search= '%'+term+'%')))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        traceback.print_exc()
        return 'Error submitting operation: %s' % e, 500


def search_table_by_cid(table_name, term):
    conn = connect()
    cur = connect().cursor()
    try:
        cur.execute("""
         SELECT * FROM %s WHERE CID = %s;
         """,
         (table_name, term))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        traceback.print_exc()
        return 'Error submitting operation: %s' % e, 500