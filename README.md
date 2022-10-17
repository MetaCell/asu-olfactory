*Cloud harness deployment*

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

