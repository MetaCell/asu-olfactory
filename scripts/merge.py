import os
import pandas as pd

# 1. defines path to csv files
path = "/Users/infectuz/Downloads/CID/"

# 2. creates list with files to merge based on name convention
file_list = [path + f for f in os.listdir(path) if f.startswith('CID-head')]
prev_reader = None
# 4. reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
for file in sorted(file_list):
    column_name = os.path.basename(file)
    reader = pd.read_csv(file, names=['CID', column_name], sep='\t', header=None)
    if prev_reader is not None:
      reader = pd.merge(prev_reader, reader, how='left', on='CID')
    prev_reader = reader

print(prev_reader)
