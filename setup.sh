minikube start --driver=docker
minikube addons enable ingress

kubectl create ns asu
eval $(minikube docker-env)

harness-deployment cloud-harness . -n asu --domain asu.local -i pub-chem-index -e local -dtls -u 
eval $(ssh-agent)
skaffold dev