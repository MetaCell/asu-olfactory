ls -la /data/db/
cd /data/db/
[ -d "CID-Synonym-unfiltered" ] && echo "CID files exist. Skipping download" || wget -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz && gunzip CID-Synonym-unfiltered.gz
ls -la /data/db/


python3 /normalize.py CID-Synonym-unfiltered /data/db/CID_Chunks
python3 /populateTable.py /data/db/CID_Chunks