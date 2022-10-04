pwd
ls -ls
ls -la /tmp/
cd /tmp/
ls -ls
[ -d "CID-Synonym-unfiltered" ] && echo "CID files exist. Skipping download" ||>
[ -d "CID-Synonym-filtered" ] && echo "CID files exist. Skipping download" || w>
[ -d "CID-IUPAC" ] && echo "CID files exist. Skipping download" || wget -q -nc >
[ -d "CID-MeSH" ] && echo "CID files exist. Skipping download" || wget -q -nc h>
[ -d "CID-InChI-Key" ] && echo "CID files exist. Skipping download" || wget -q >
[ -d "CID-Title" ] && echo "CID files exist. Skipping download" || wget -q -nc >
[ -d "CID-SMILES" ] && echo "CID files exist. Skipping download" || wget -q -nc>

ls -la /tmp/
pwd

python3 /populate_parallel.py /tmp /tmp/CID