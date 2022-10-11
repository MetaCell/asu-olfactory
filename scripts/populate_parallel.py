import pandas as pd
import os
import sys
import csv
import logging
import dask.dataframe as dd
import asyncio
import aiopg
import shutil
import stat
from functools import reduce

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

#
# WARNING!!! use head command on files for debugging
# head -n 500000 CID-SMILES > CID-SMILES-head
#

#"https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz"

added_col_dic = {
  "CID-InChI-Key": ["CID", "InChI", "Key"],
  "CID-Mass": ["CID", "Molecule", "Mass1", "Mass2"],
  "CID-PMID": ["CID", "PMID"],
  "CID-Parent": ["CID", "Parent"],
  "CID-Patent": ["CID", "Patent"],
  "CID-SID": ["CID", "SID"],
  "CID-MeSH": ["CID", "MeSH"],
  "CID-SMILES": ["CID", "MID", "SMILES"],
  "CID-Synonym-filtered": ["CID", "Synonym"],
  "CID-Synonym-unfiltered": ["CID", "Syn"],
  "CID-Title": ["CID", "Title"],
  "CID-IUPAC": ["CID", "IUPAC"]
}

async def execute_sql(pool, sql):
  #print(sql)
  async with pool.acquire() as conn:
    async with conn.cursor() as cur:
      await cur.execute(sql)

def change_permissions_recursive(path, mode):
  for root, dirs, files in os.walk(path, topdown=False):
    for file in [os.path.join(root, f) for f in files]:
      if file.startswith('export-'):
          os.chmod(file, mode)
  #os.chmod(path, mode)

async def create_table(pool, table_name):
  #Populate GIN indexed table, this will take about 30 minutes.
  column_names = added_col_dic[table_name]
  column_names = [x.upper() for x in column_names]
  main_column  = column_names[1].upper()
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
      CID INTEGER NOT NULL PRIMARY KEY,
      %s
  )
  """ % (table_name, str_column_names)  #better management

  await execute_sql(pool, sql_copy)

  logging.info("Table created")

async def bulk_insert(chunk, table_name, pool):

  async with pool.acquire() as conn:
    async with conn.cursor() as cur:
      sql_insert = ','.join(cur.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s)", x) for x in chunk)
      sql_s      = "INSERT INTO %s VALUES %s" % table_name, sql_insert
      cur.execute(sql_s) 

async def create_indexes(table_name, pool):
  column_names = added_col_dic[table_name]
  column_names = [x.upper() for x in column_names]
  main_column  = column_names[1].upper()

  await execute_sql(pool, "CREATE EXTENSION IF NOT EXISTS pg_trgm")
  sql_copy = '''CREATE INDEX IF NOT EXISTS idx_gin ON %s USING gin (%s gin_trgm_ops);''' % (table_name, main_column)
  await execute_sql(pool, sql_copy)
  sql_copy = '''CREATE INDEX IF NOT EXISTS cid_idx ON %s (CID);''' % table_name
  await execute_sql(pool, sql_copy) 
  pool.close()

async def go():
  path = os.path.dirname(os.path.realpath(__file__)) + "/db"
  logging.info("Populating table using files from %s", path)
  dns = 'dbname=asu user=postgres password=postgres host=localhost'

  file_list = [path + '/' + f for f in os.listdir(path) if f.startswith('CID-')]
  for file in sorted(file_list):
      file_name = os.path.basename(file)
      column_name      = ['CID', file_name]
      types            = { file_name: 'string', 'CID': 'Int64' }
      if file_name in added_col_dic:
        column_name = added_col_dic[file_name]
        types = { 'CID': 'Int64' }
        for c in column_name:
          if c is not 'CID':
            types[c] = 'string'
      
      pool = await aiopg.create_pool(dns)

      await create_table(pool, file_name)

      chunksize = 10 ** 8
      for chunk in pd.read_csv(file
                              , quoting=csv.QUOTE_NONE
                              , names=column_name
                              , chunksize=chunksize
                              , dtype=types
                              , sep='\t'
                              , header=None
                              , on_bad_lines='skip'):

        await bulk_insert(chunk, file_name, pool)

      await create_indexes(pool, file_name)


loop = asyncio.get_event_loop()
loop.run_until_complete(go())  