#!/bin/bash

cd /data/db/

tablename=${filename%".gz"}
if [[ "${filename}" == *.gz ]];
then
    [[ ! -f "${tablename}" ]] && wget -O - -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/${filename} | gunzip -c > ${tablename}
else
    [[ ! -f "${tablename}" ]] && wget -O - -q -nc https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/${filename} > ${tablename}
fi

ls -lah

python3 /populate_parallel.py /data/db/${tablename}
