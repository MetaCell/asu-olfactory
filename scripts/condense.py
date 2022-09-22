import os
import pandas as pd
import dask.dataframe as dd
import csv

file = "/Users/infectuz/Downloads/CID/text_index/CID-Synonym-filtered"

reader = dd.read_csv(file, quoting=csv.QUOTE_NONE, names=['CID-Synonym-filtered'], sep='\t', header=None)
output_df = {}

cid_column_indexes = reader.index.unique()

for index in cid_column_indexes:
  sub_df = reader.loc[index]
  csv_column = sub_df['CID-Synonym-filtered'].str.cat(sep=' ')
  output_df[index] = csv_column

output_df.to_csv("merged-syn.csv")
print(output_df)
print("Completed")