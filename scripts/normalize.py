import pandas as pd
import os
import csv
import codecs

#"https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz"

chunk_size=50000

added_col_dic = {
    "CID-InChI-Key": ["InChI", "Key"],
    "CID-Mass": ["Molecule", "Mass1", "Mass2"],
    "CID-PMID": ["CID-PMID", "CID-PMID-2"],
    "CID-Parent": ["CID-Parent"],
    "CID-Patent": ["CID-Patent"],
    "CID-SID": ["CID-SID"],
    "CID-MeSH": ["CID-MeSH"],
    "CID-SMILES": ["CID-SMILES"],
    "CID-Synonym-filtered": ["CID-Synonym-filtered"],
    "CID-Title": ["CID-Title"]
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

directory = '../CID'
file_list = [directory + f for f in os.listdir(directory) if f.startswith('CID-')]

for file in sorted(file_list):
      file_name = os.path.basename(file)
      column_name      = ['CID', file_name]
      types            = { file_name: 'string', 'CID': 'Int64' }
      if file_name in added_col_dic:
        column_name = ['CID'] + added_col_dic[file_name]
        types = { 'CID': 'Int64' }
        for c in column_name:
          if c is not 'CID':
            types[c] = 'string'
          
      print("Reading : " + file_name)
      for chuck in pd.read_csv(file, quoting=csv.QUOTE_NONE, names=column_name, dtype=types, sep='\t', header=None):
        chunk = tidy_split(chunk, 'Syn', sep=',', keep=False)
        folder_path = '../CID_Chunks/'+file_name
        isExist = os.path.exists(folder_path)

        if not isExist:
            # Create a new directory because it does not exist 
            os.makedirs(folder_path)
        chunk.to_csv(folder_path+'/'+file_name+'_'+str(chunk_n)+'.csv', index=False)
        chunk_n = chunk_n + 1
      chunk_n = 0