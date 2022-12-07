# ASU Olfactory Instructions

## Endpoints Use

All available endpoints are available here https://pubchem.olfactory.dev.metacell.us/ui/

For summary:
- molecules/synonyms/{CID/TEXT}
- molecules/synonyms_unfiltered/{CID/TEXT}
- molecules/mesh/{CID/TEXT}
- molecules/iupac/{CID/TEXT}
- molecules/mass/{CID/TEXT}
- molecules/component/{CID/TEXT}
- molecules/title/{CID/TEXT}
- molecules/smiles/{CID/TEXT}
- molecules/pmid/{CID/TEXT}
- molecules/sid/{CID/TEXT}
- molecules/parent/{CID/TEXT}
- molecules/patent/{CID/TEXT}
- molecules/inchi/{CID/TEXT}

Each of the above endpoints can be followed by 
- /properties/{FILES_LIST}

Where {FILES_LIST} is comma separated list of the PubChem file names.
E.g. 
 - /properties/synonym_filtered,synonym_unfiltered,mesh,title,iupac

Any of the endpoints above can be followed by Query Parameter 
```
?exactMatch=True
```
Which will return the exact matches of the search.

Example Searches returning exact matches:
- https://pubchem.olfactory.dev.metacell.us/molecules/mesh/chlorin?exactMatch=True
- https://pubchem.olfactory.dev.metacell.us/molecules/mesh/chlorin/properties/synonym_filtered,title,iupac?exactMatch=True

By default, not using the query parameter will return all results regardless of exact match.
- https://pubchem.olfactory.dev.metacell.us/molecules/mesh/chlorin
- https://pubchem.olfactory.dev.metacell.us/molecules/mesh/chlorin?exactMatch=False

***Names of tables that can be passed for cross table lookup.***
- InChI_Key
- Mass
- PMID
- Parent
- Patent
- SID
- MeSH
- SMILES
- Synonyms_filtered
- Synonym_unfiltered
- Title
- IUPAC
- Component


## Cloud harness deployment

```

Install cloud-harness inside root folder. Follow ReadMe instructions on cloud-harness to install all requirements, and run all the instructions on there.

minikube start --driver=docker
minikube addons enable ingress

kubectl create ns asu
eval $(minikube docker-env)

harness-deployment cloud-harness . -n asu --domain asu.local -i pub-chem-index -e local -dtls -u 
eval $(ssh-agent)
skaffold dev



Running Dockers :

Running Postgress Image:
- docker volume create asu_volume
- docker build -t asu_db .
- docker run --name asu_db_container -e POSTGRES_PASSWORD=password -e POSTGRES_USER=postgres -p 5432:5432 -v asu_volume:/sharedVol -d asu_d

Running Population Scripts Image : 
- docker build -t asu_app .
- docker run --name asu_app_container -v asu_volume:/CID_Chunks -d asu_app

```

*Local client installation*

Start the proxy server first to avoid CORS blocking from localhost

```
cd ..\api-call-example-server
npm install express
node app.js
```

This will get the server proxy running on localhost:3010
Now build and start the actual client which uses the proxy server

```
cd ..\api-call-example-client
npm install
npm run build 
npm start
```

