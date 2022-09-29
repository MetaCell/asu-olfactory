ls -la /data/db/
cd /data/db
mkdir files
cd files
[ -d "CID-Synonym-unfiltered" ] && echo "CID files exist. Skipping download" || wget -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz && gunzip CID-Synonym-unfiltered.gz
[ -d "CID-Synonym-filtered" ] && echo "CID files exist. Skipping download" || wget -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-filtered.gz && gunzip CID-Synonym-filtered.gz
[ -d "CID-IUPAC" ] && echo "CID files exist. Skipping download" || wget -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-IUPAC.gz && gunzip CID-IUPAC.gz
[ -d "CID-MeSH" ] && echo "CID files exist. Skipping download" || wget -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-MeSH.gz && gunzip CID-MeSH.gz
[ -d "CID-InChI-Key" ] && echo "CID files exist. Skipping download" || wget -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-InChI-Key.gz && gunzip CID-InChI-Key.gz
[ -d "CID-Title" ] && echo "CID files exist. Skipping download" || wget -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Title.gz && gunzip CID-Title.gz
[ -d "CID-SMILES" ] && echo "CID files exist. Skipping download" || wget -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-SMILES.gz && gunzip CID-SMILES.gz

ls -la /data/db/files


python3 /normalize.py /data/db/files /data/db/CID_Chunks
python3 /populateTable.py /data/db/CID_Chunks