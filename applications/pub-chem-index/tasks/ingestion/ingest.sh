pwd
ls -ls
ls -la /data/db/
cd /data/db/
ls -ls
[ -d "CID-MeSH" ] && echo "CID files exist. Skipping download" || wget -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-MeSH

ls -la /data/db/CID-MeSH
pwd

python3 /populate_parallel.py CID-MeSH /data/db/CID