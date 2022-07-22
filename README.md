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
