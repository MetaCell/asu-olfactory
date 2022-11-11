import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=54320,
    dbname='asu',
    user='postgres',
    password='postgres',
)
cur = conn.cursor()
cur.execute("CREATE TABLE t_hash AS SELECT id, md5(id::text) FROM generate_series(1, 50000000) AS id")
cur.execute("CREATE EXTENSION pg_trgm")
cur.execute("CREATE INDEX idx_gin ON t_hash USING gin (md5 gin_trgm_ops);")
cur.execute("SELECT * FROM t_hash WHERE md5 LIKE '%e2345679a%';;")
result = cur.fetchone()
print(result)
conn.commit()
cur.close()
conn.close()
