pwd
ls -la /data/db/
cd /data/db/
[ -d "CID-MeSH" ] && echo "CID files exist. Skipping download" || wget -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-MeSH
ls -la /data/db
pwd

python3 /populate_parallel.py /data/db /data/db/CID