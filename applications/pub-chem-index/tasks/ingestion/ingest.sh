pwd
ls -ls
ls -la /tmp/
cd /tmp/
ls -ls
[ -d "CID-Synonym-filtered" ] && echo "CID files exist. Skipping download" || wget -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-filtered.gz && gunzip CID-Synonym-filtered.gz
[ -d "CID-MeSH" ] && echo "CID files exist. Skipping download" || wget -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-MeSH
[ -d "CID-SMILES" ] && echo "CID files exist. Skipping download" || wget -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-SMILES.gz && gunzip CID-SMILES.gz

ls -la /tmp/
pwd

python3 /populate_parallel.py /tmp /tmp/CID