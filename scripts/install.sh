wget https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz
gunzip CID-Synonym-unfiltered.gz
mkdir CID_Chunks
python3 scripts/normalize.py
python3 scripts/populateTable.py