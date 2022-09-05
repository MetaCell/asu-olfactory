import pandas as pd 

# files =['CID-Component:Component'
#       , 'CID-IUPAC:IUPAC'
#       , 'CID-InChI-Key:InChI'
#       , 'CID-Mass:Mass'
#       , 'CID-MeSH:MeSH'
#       , 'CID-PMID:PMID'
#       , 'CID-Parent:Parent'
#       , 'CID-Patent:Parent'
#       , 'CID-SID:SID'
#       , 'CID-SMILES:SMILES']

files =['CID-SMILES:SMILES']

file_name = '/CID/CID-Synonym-unfiltered'
df_base = pd.read_csv(file_name, header=None, encoding="ISO-8859-1", index_col='CID')

for f in files:
  parts = f.split(':')
  file_name_part   = f[0]
  column_name_part = f[1]
  file_name = '/CID/%s' % file_name_part
  df_merge = pd.read_csv(file_name, header=None, encoding="ISO-8859-1", index_col='CID')
  pd.merge(df_base, df_merge, how='inner', on=['CID'])

df_base.to_csv(name="merged.csv")

    