```

Install cloud-harness inside root folder. Follow ReadMe instructions on cloud-harness to install all requirements, and run all the instructions on there.

minikube start --driver=docker
minikube addons enable ingress

kubectl create ns ifn
eval $(minikube docker-env)

harness-deployment cloud-harness . -n asu --domain asu.local -i pub-chem-index -e local -dtls -u 

skaffold dev
```
