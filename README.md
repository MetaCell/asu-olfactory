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

