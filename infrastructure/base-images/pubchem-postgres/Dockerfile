FROM postgres:14
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
      apt-get -y install sudo

RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

USER root
CMD /bin/bash

# Update Ubuntu Software repository
RUN apt -y install python3-pip wget 
RUN pip install pandas psycopg2-binary wheel
RUN apt update
RUN dpkg --configure -a
RUN apt-get -y install -f git

WORKDIR $HOME/workspace

RUN git clone -b main https://github.com/MetaCell/asu-olfactory.git

WORKDIR $HOME/workspace/asu-olfactory
RUN wget https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz
RUN gunzip CID-Synonym-unfiltered.gz
RUN mkdir CID_Chunks
RUN python3 scripts/normalize.py
RUN python3 scripts/populateTable.py
RUN less CID_Chunks/CID-Synonym-unfiltered_1.csv