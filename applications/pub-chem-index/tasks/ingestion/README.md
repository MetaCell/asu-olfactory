# Development run local

run the bash script "portforward.sh" (see root of this repository) to forward the cloud postgresql 5432 port to the local machine
```bash
source portforward.sh
```

this script assumes that the pods are running in the `asu` namespace

then create a folder `/data/db` and make sure your user has write permissions\
```bash
sudo mkdir -p /data/db
chown -R ${USER} /data/db
```

create & activate your OLFactory virtualenv

install the ingestion requirements

```
pip install -r requirements.txt
```

run the ingestion script
```bash
chmod +x ingest.sh
filename="<filename>" ./ingest.sh
```
