import pandas as pd
import os
import csv
import logging
import dask.dataframe as dd
import asyncio
import aiopg
import shutil

#
# WARNING!!! use head command on files for debugging
# head -n 500000 CID-SMILES > CID-SMILES-head
#

#"https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz"

added_col_dic = {
  "CID-InChI-Key": ["CID", "InChI", "Key"],
  "CID-Mass": ["CID", "Molecule", "Mass1", "Mass2"],
  "CID-PMID": ["CID", "CID-PMID"],
  "CID-Parent": ["CID", "CID-Parent"],
  "CID-Patent": ["CID", "CID-Patent"],
  "CID-SID": ["CID", "CID-SID"],
  "CID-MeSH": ["CID", "CID-MeSH"],
  "CID-SMILES": ["CID", "CID-SMILES"],
  "CID-Synonym-filtered": ["CID", "Syn"],
  "CID-Synonym-unfiltered": ["CID", "Syn"],
  "CID-Title": ["CID", "CID-Title"],
  "CID-IUPAC": ["CID", "CID-IUPAC"]
}

async def execute_sql(pool, sql):
  #print(sql)
  async with pool.acquire() as conn:
    async with conn.cursor() as cur:
      await cur.execute(sql)

async def populate_table(table_name, path, dns):
  #Populate GIN indexed table, this will take about 30 minutes.
  pool = await aiopg.create_pool(dns)

  table_name = table_name.replace("-", "_")
  sql_copy = """
  CREATE TABLE IF NOT EXISTS %s (
      CID VARCHAR NOT NULL,
      Value VARCHAR
  )
  """ % table_name #better management
  async with pool.acquire() as conn:
    async with conn.cursor() as cur:
      await cur.execute(sql_copy)

  logging.info("Table created")

  # loop over the list of csv files
  file_list = [path + f for f in os.listdir(path) if f.startswith('export-')]

  #!!!! RUN IN PARALLEL ??

  # pool.map(ins_into_db, [i+1 for i in range(7)])
  # pool.close()
  # pool.join()


  #with Pool(processes=len(my_queries)) as pool:
      #pool.map(partial(execute_query,rs_conn_string), my_queries)

  sql_list = []
  for f in file_list:
    logging.info("Ingesting file %s", f)
    sql_copy = '''
        COPY %s
        FROM '%s'
        DELIMITER ',' CSV HEADER;
        '''  % (table_name , f)
    logging.info("Query is %s", sql_copy)
    sql_list.append(sql_copy)
    
  await asyncio.gather(*[execute_sql(pool, sql_list[i]) for i in range(len(sql_list))])

  await cur.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
  sql_copy = '''CREATE INDEX IF NOT EXISTS idx_gin ON %s USING gin (Synonym gin_trgm_ops);''' % table_name
  await cur.execute(sql_copy)
  sql_copy = '''CREATE INDEX IF NOT EXISTS cid_idx ON %s (CID);''' % table_name
  await cur.execute(sql_copy) 

async def go():
  path = os.path.dirname(os.path.realpath(__file__)) + "/data/db"
  logging.info("Populating table using files from %s", path)
  dns = 'dbname=asu user=postgres password=postgres host=localhost'

  file_list = [path + '/' + f for f in os.listdir(path) if f.startswith('CID-SMILES-head')]
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
                      , blocksize=1e6 #1MB
                      , dtype=types
                      , sep='\t'
                      , header=None
                      , on_bad_lines='skip')

      output = path + '/tmp/'
      #delete tmp
      #hutil.rmtree(output)
      #spit out and populate
      df.to_csv(output + "export-*.csv")
      await populate_table(file_name, output, dns) 

loop = asyncio.get_event_loop()
loop.run_until_complete(go())  