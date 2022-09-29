import pandas as pd
import os
import csv
import codecs

#"https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz"

chunk_size=50000

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

def tidy_split(df, column, sep=',', keep=False):
    """
    Split the values of a column and expand so the new DataFrame has one split
    value per row. Filters rows where the column is missing.

    Params
    ------
    df : pandas.DataFrame
        dataframe with the column to split and expand
    column : str
        the column to split and expand
    sep : str
        the string used to split the column's values
    keep : bool
        whether to retain the presplit value as it's own row

    Returns
    -------
    pandas.DataFrame
        Returns a dataframe with the same columns as `df`.
    """
    indexes = list()
    new_values = list()
    df = df.dropna(subset=[column])
    for i, presplit in enumerate(df[column].astype(str)):
        indexes.append(i)
        new_values.append(presplit)
    new_df = df.iloc[indexes, :].copy()
    new_df[column] = new_values
    return new_df

chunk_n = 1

directory = '/CID'
file_list = [directory + '/' + f for f in os.listdir(directory) if f.startswith('CID-')]

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
          
      print("Reading : " + file_name)
      print("Using column names : " + str(column_name))
      folder_path = '/CID_Chunks/'+file_name
      isExist = os.path.exists(folder_path)
      #print("chunk " + chunk)        
      if not isExist:
          # Create a new directory because it does not exist
          print("Creating directory " + folder_path) 
          os.makedirs(folder_path)
      doc = pd.read_csv(codecs.open(file,'rU','UTF-8'), quoting=csv.QUOTE_NONE, names=column_name, chunksize=chunk_size, dtype=types, sep='\t', header=None, on_bad_lines='skip')
      for chunk in doc:
        #print("first chunk")
        chunk = tidy_split(chunk, 'CID', sep=',', keep=False)
        chunk.to_csv(folder_path+'/'+file_name+'_'+str(chunk_n)+'.csv', index=False)
        chunk_n = chunk_n + 1
      chunk_n = 0