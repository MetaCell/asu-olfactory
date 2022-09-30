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

async def populate_table(table_name, path, dns):
  #Populate GIN indexed table, this will take about 30 minutes.
  pool = await aiopg.create_pool(dns)

  column_names = added_col_dic[table_name]
  main_column = column_names[1]

  str_column_names =""

  for i in column_names:
    if i != "CID":
      str_column_names+=i + ' VARCHAR,'

  str_column_names = str_column_names[:len(str_column_names)-1]

  table_name = table_name.replace("-", "_")

  sql_copy = """
  DROP TABLE IF EXISTS %s
  """ % (table_name)  #better management

  await execute_sql(pool, sql_copy)

  sql_copy = """
  CREATE TABLE %s (
      CID VARCHAR NOT NULL,
      %s
  )
  """ % (table_name, str_column_names)  #better management

  await execute_sql(pool, sql_copy)

  logging.info("Table created")

  # loop over the list of csv files
  file_list = [path + f for f in os.listdir(path) if f.startswith('export-')]

  sql_list = []
  for f in file_list:
    logging.info("Ingesting file %s", f)
    sql_copy = '''
        COPY %s
        FROM '%s'
        DELIMITER '\t' CSV HEADER;
        '''  % (table_name , f)
    logging.info("Query is %s", sql_copy)
    await execute_sql(pool, sql_copy)
    
  await execute_sql(pool, "CREATE EXTENSION IF NOT EXISTS pg_trgm")
  sql_copy = '''CREATE INDEX IF NOT EXISTS idx_gin ON %s USING gin (%s gin_trgm_ops);''' % (table_name, main_column)
  await execute_sql(pool, sql_copy)
  sql_copy = '''CREATE INDEX IF NOT EXISTS cid_idx ON %s (CID);''' % table_name
  await execute_sql(pool, sql_copy) 
  pool.close()

async def go():
  path = os.path.dirname(os.path.realpath(__file__)) + "/../CID"
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

      df = dd.read_csv(file
                      , quoting=csv.QUOTE_NONE
                      , names=column_name
                      , blocksize=150e6 #150MB
                      , dtype=types
                      , sep='\t'
                      , header=None
                      , on_bad_lines='skip')

      output = '/tmp/CID/' + file_name
      #delete tmp
      if os.path.isdir(output):
        shutil.rmtree(output)
      #spit out and populate
      df.to_csv(output + "export-*.csv", sep='\t', index=False)

      change_permissions_recursive(output, stat.S_IROTH)

      await populate_table(file_name, output, dns) 

loop = asyncio.get_event_loop()
loop.run_until_complete(go())  