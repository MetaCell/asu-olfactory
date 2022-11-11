import pandas as pd
import numpy as np
import os
import sys
import csv
import logging
import asyncio
import aiopg
import psycopg2

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

#
# WARNING!!! use head command on files for debugging
# head -n 500000 CID-SMILES > CID-SMILES-head
#

#"``https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/`CID-Synonym-unfiltered.gz"

added_col_dic = {
  "CID-InChI-Key": ["CID", "InChI", "Key"],
  "CID-Mass": ["CID", "Molecule", "Mass1", "Mass2"],
  "CID-PMID": ["CID", "PMID"],
  "CID-Parent": ["CID", "Parent"],
  "CID-Patent": ["CID", "Patent"],
  "CID-SID": ["CID", "SID"],
  "CID-MeSH": ["CID", "MeSH"],
  "CID-SMILES": ["CID", "SMILES"],
  "CID-Synonym-filtered": ["CID", "Synonym"],
  "CID-Synonym-unfiltered": ["CID", "Syn"],
  "CID-Title": ["CID", "Title"],
  "CID-IUPAC": ["CID", "IUPAC"]
}

gin_indexes_tables = ['CID-Title', 'CID-MeSH', 'CID-UIPAC', 'CID-InChI-Key', 'CID-Synonym-filtered']

async def execute_sql(pool, sql):
  #print(sql)
  async with pool.acquire() as conn:
    async with conn.cursor(timeout=5000000) as cur:
      await cur.execute(sql)

async def create_table(pool, table_name):
  #Populate GIN indexed table, this will take about 30 minutes.
  column_names = added_col_dic[table_name]
  column_names = [x.upper() for x in column_names]
  table_name   = table_name.replace("-", "_").upper()

  str_column_names =""

  for i in column_names:
    if i != "CID":
      str_column_names+=i + ' VARCHAR,'

  str_column_names = str_column_names[:len(str_column_names)-1]

  sql_copy = """
  DROP TABLE IF EXISTS %s
  """ % (table_name)  #better management

  await execute_sql(pool, sql_copy)

  sql_copy = """
  CREATE TABLE %s (
      CID INTEGER NOT NULL,
      %s
  )
  """ % (table_name, str_column_names)  #better management

  await execute_sql(pool, sql_copy)

  logging.info("Table created %s ", table_name)

async def bulk_insert(chunk, table_name, pool):

  async with pool.acquire() as conn:
    async with conn.cursor() as cur:
      template   = ','.join(['%s'] * len(chunk))
      sql_insert = 'insert into '+table_name.lower()+' VALUES {}'.format(template)
      sql_insert_values = cur.mogrify(sql_insert, chunk).decode('utf8')
      #print()
      #await cur.execute(sql_insert_values) 
      await execute_sql(pool, sql_insert_values)


async def create_indexes(pool, table_name, create_gin):
  column_names = added_col_dic[table_name]
  column_names = [x.upper() for x in column_names]
  main_column  = column_names[1].lower()
  table_name   = table_name.replace("-", "_").lower()

  if create_gin:
    await execute_sql(pool, "CREATE EXTENSION IF NOT EXISTS pg_trgm")
    sql_copy = '''CREATE INDEX IF NOT EXISTS idx_gin_%s ON %s USING gin (%s gin_trgm_ops);''' % (table_name, table_name, main_column)
    await execute_sql(pool, sql_copy)

  sql_copy = '''CREATE INDEX IF NOT EXISTS cid_idx_%s ON %s (CID);''' % (table_name, table_name)
  await execute_sql(pool, sql_copy) 
  pool.close()

async def go():

  psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

  path = os.path.dirname(os.path.realpath(__file__)) + "/db"
  logging.info("Populating table using files from %s", path)
  dns = 'dbname=asu user=postgres password=postgres host=localhost'

  file_list = [path + '/' + f for f in os.listdir(path) if f.startswith('CID-')]
  for file in sorted(file_list):
      file_name = os.path.basename(file)
      column_name      = ['CID', file_name]
      types            = { file_name: 'string', 'CID': 'Int64' }
      column_names = added_col_dic[file_name]
      #column_names = [x.upper() for x in column_names]
      main_column  = column_names[1] #.upper()
      gin_indexed = file_name in gin_indexes_tables
      
      if file_name in added_col_dic:
        column_name = added_col_dic[file_name]
        types = { 'CID': 'Int64' }
        for c in column_name:
          if c is not 'CID':
            types[c] = 'string'
      
      pool = await aiopg.create_pool(dns)

      await create_table(pool, file_name)

      encoding = None
      if file_name == 'CID-Title':
        encoding = 'Latin'
        
      chunksize = 1000000
      for chunk in pd.read_csv(file
                              , quoting=csv.QUOTE_NONE
                              , names=column_name
                              , chunksize=chunksize
                              , dtype=types
                              , sep='\t'
                              , header=None
                              , encoding = encoding
                              , on_bad_lines='skip'):


        chunk = chunk.dropna()
        data = list(chunk.itertuples(index=False))
        await bulk_insert(data, file_name.replace("-", "_"), pool)

      await create_indexes(pool, file_name, gin_indexed)


loop = asyncio.get_event_loop()
loop.run_until_complete(go())  