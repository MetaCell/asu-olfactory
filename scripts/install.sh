wget https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz
gunzip CID-Synonym-unfiltered.gz
mkdir CID_Chunks
python3 scripts/normalize.py
ls
cd CID_Chunks
ls
cd ..
python3 scripts/populateTable.py "/workspace/asu-olfactory/CID_Chunks/"