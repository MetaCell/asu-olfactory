FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
      apt-get -y install sudo

RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

USER root
CMD /bin/bash

# Update Ubuntu Software repository
RUN apt -y install python3-pip wget
RUN pip install pandas psycopg2-binary wheel
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get -y install postgresql git-all

WORKDIR $HOME/workspace

RUN git clone -b main https://github.com/MetaCell/asu-olfactory.git
RUN cd asu-olfactory && ls
WORKDIR $HOME/workspace/asu-olfactory
RUN wget https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz
RUN ls && gunzip CID-Synonym-unfiltered.gz
RUN mkdir CID_Chunks
RUN ls && python3 scripts/normalize.py
RUN python3 scripts/populateTable.py
RUN CID_Chunks && ls
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

