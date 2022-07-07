FROM python:3.9
ADD . /
ENV shared_directory /CID_Chunks

RUN apt-get update && \
      apt-get -y install sudo

USER root

# Update Ubuntu Software repository
RUN apt -y install python3-pip wget
RUN pip install pandas psycopg2-binary wheel

RUN wget https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz
RUN gunzip CID-Synonym-unfiltered.gz

RUN pwd
COPY populateTable.py /populateTable.py
COPY install.sh /install.sh
COPY normalize.py /normalize.py
RUN ls
RUN pwd
RUN mkdir /chunks
RUN python3 normalize.py
RUN ls /chunks && ls ..

CMD ["sh", "-c", "python3 populateTable.py $shared_directory"]