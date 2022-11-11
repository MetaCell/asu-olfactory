import os
import pandas as pd
import dask.dataframe as dd
import csv
from dask.distributed import Client
from dask.diagnostics import ProgressBar

run_head = False

if run_head:
  added_col_dic = {
    "CID-head-InChI-Key": ["InChI", "Key"],
    "CID-head-Mass": ["Molecule", "Mass1", "Mass2"],
    "CID-head-PMID": ["CID-PMID", "CID-PMID-2"],
    "CID-head-Parent": ["CID-Parent"],
    "CID-head-Patent": ["CID-Patent"],
    "CID-head-SID": ["CID-SID"],
    "CID-head-MeSH.txt": ["CID-MeSH.txt"],
    "CID-head-SMILES": ["CID-SMILES"],
    "CID-head-Synonym-filtered": ["CID-Synonym-filtered"],
    "CID-head-Title": ["CID-Title"]
  }
else:
  added_col_dic = {
    "CID-InChI-Key": ["InChI", "Key"],
    "CID-Mass": ["Molecule", "Mass1", "Mass2"],
    "CID-PMID": ["CID-PMID", "CID-PMID-2"],
    "CID-Parent": ["CID-Parent"],
    "CID-Patent": ["CID-Patent"],
    "CID-SID": ["CID-SID"],
    "CID-MeSH.txt": ["CID-MeSH.txt"],
    "CID-SMILES": ["CID-SMILES"],
    "CID-Synonym-filtered": ["CID-Synonym-filtered"],
    "CID-Title": ["CID-Title"]
  }

if __name__ == '__main__':   
  #df = dd.read_csv('merged.csv/*.part')
  ProgressBar().register() 
  client = Client(n_workers=4, threads_per_worker=1, memory_limit="6GB")

  # 1. defines path to csv files
  if run_head:
    path = "/Users/infectuz/Downloads/CID/head/"
  else:
    path = "/Users/infectuz/Downloads/CID/text_index/head/"

  # 2. creates list with files to merge based on name convention
  file_list = [path + f for f in os.listdir(path) if f.startswith('CID-')]
  prev_reader = None
  # 4. reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
  for file in sorted(file_list):
      column_name_file = os.path.basename(file)
      column_name      = ['CID', column_name_file]
      types            = { column_name_file: 'string', 'CID': 'Int64' }
      if column_name_file in added_col_dic:
        column_name = ['CID'] + added_col_dic[column_name_file]
        types = { 'CID': 'Int64' }
        for c in column_name:
          if c is not 'CID':
            types[c] = 'string'
          
      reader = dd.read_csv(file, quoting=csv.QUOTE_NONE, names=column_name, dtype=types, sep='\t', header=None)
      if prev_reader is not None:
          reader = dd.merge(prev_reader, reader, how='left', on='CID')
      prev_reader = reader

  with ProgressBar():
    prev_reader.to_csv("merged.csv")
    print("Completed")
