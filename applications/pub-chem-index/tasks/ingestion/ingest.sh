#!/bin/bash

pwd
ls -lah /data/db/
cd /data/db/

[ ! -f "CID-Synonym-filtered" ] && wget -O - -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-filtered.gz | gunzip -c > CID-Synonym-filtered
[ ! -f "CID-IUPAC" ] && wget -O - -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-IUPAC.gz | gunzip -c > CID-IUPAC
[ ! -f "CID-MeSH" ] && wget -O - -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-MeSH > CID-MeSH
[ ! -f "CID-InChI-Key" ] && wget -O - -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-InChI-Key.gz | gunzip -c > CID-InChI-Key
[ ! -f "CID-Title" ] && wget -O - -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Title.gz | gunzip -c > CID-Title
[ ! -f "CID-SMILES" ] && wget -O - -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-SMILES.gz | gunzip -c > CID-SMILES

ls -lah /data/db
pwd

python3 /populate_parallel.py /data/db /data/db/CID
