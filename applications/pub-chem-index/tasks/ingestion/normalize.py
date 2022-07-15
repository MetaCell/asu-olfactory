import pandas as pd 
import codecs
import sys
import os
import logging

chunk_size=50000

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

file_name = sys.argv[1]
dest_folder = sys.argv[2]
logging.info("Normalizing files from %s to %s")
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)
doc = codecs.open(file_name,'rU','UTF-8') #open for reading with "universal" type set

reader = pd.read_csv(doc, sep = None, iterator = True)
inferred_sep = reader._engine.data.dialect.delimiter

for chunk in list(pd.read_csv(doc, sep=inferred_sep, chunksize=chunk_size, header=None, names=['CID', 'Syn'])):
  chunk = tidy_split(chunk, 'Syn', sep=',', keep=False)
  chunk.to_csv(dest_folder + '/CID-Synonym-unfiltered_'+str(chunk_n)+'.csv', index=False)
  chunk_n = chunk_n + 1
    