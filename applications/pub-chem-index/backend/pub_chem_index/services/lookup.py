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
        tquery = "select * from {}".format(table_name)
        cur.execute(tquery)
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
        table_query =  "SELECT * FROM {0} WHERE {1} LIKE '{2}';".format(table_name, key, term)
        cur.execute(table_query)
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
        table_query =  "SELECT * from {0} WHERE CID = '{1}'".format(table_name, term)
        cur.execute(table_query)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        traceback.print_exc()
        return 'Error submitting operation: %s' % e, 500
