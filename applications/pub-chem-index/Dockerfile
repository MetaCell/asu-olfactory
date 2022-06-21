# Download base image ubuntu 20.04
FROM ubuntu:20.04


# Update Ubuntu Software repository
RUN apt update
RUN sudo apt install python3-pip
RUN pip install pandas psycopg2-binary wheel
RUN sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
RUN sudo apt-get update
RUN sudo apt-get -y install postgresql

RUN git clone -b main git clone https://github.com/MetaCell/asu-olfactory.git
RUN cd asu-olfactory
RUN wget https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz
RUN gunzip CID-Synonym-unfiltered.gz
RUN mkdir CID_CHUNKS
RUN python3 scripts/populateTable.py
RUN CID_CHUNKS && ls
RUN nano CID-Synonym-unfiltered_2521.csv

RUN ../
RUN git clone https://github.com/MetaCell/cloud-harness
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh
RUN bash Miniconda3-py39_4.12.0-Linux-x86_64.sh 
RUN conda create --name ch python=3.9

RUN cd cloud-harness

RUN minikube start --driver=docker
RUN minikube addons enable ingress
RUN kubectl create ns asu
RUN eval $(minikube docker-env)
RUN harness-deployment cloud-harness . -n asu --domain asu.local -i pub-chem-index -e local -dtls -u 
RUN skaffold dev

