FROM python:3.9
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
      apt-get -y install sudo

USER root

# Update Ubuntu Software repository
RUN apt -y install python3-pip wget 
RUN pip install pandas psycopg2-binary wheel

RUN ls
RUN wget https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz
RUN gunzip CID-Synonym-unfiltered.gz

COPY populateTable.py /populateTable.py
COPY install.sh /install.sh
COPY normalize.py /normalize.py
RUN mkdir /data/db/pgdata/chunks
RUN python3 normalize.py
RUN ls /data/db/pgdata/chunks && ls ..

ENTRYPOINT [ "python3", "populateTable.py"]
