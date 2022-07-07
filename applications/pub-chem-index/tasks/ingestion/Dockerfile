FROM python:3.9
ADD . /
ENV shared_directory /CID_Chunks

RUN apt-get update && \
      apt-get -y install sudo

USER root

# Update Ubuntu Software repository
RUN apt -y install python3-pip
RUN pip install pandas psycopg2-binary wheel

#RUN wget https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-unfiltered.gz
#RUN gunzip CID-Synonym-unfiltered.gz

RUN pwd
COPY populateTable.py /populateTable.py
COPY install.sh /install.sh
COPY normalize.py /normalize.py

RUN mkdir /CID-Synonym-unfiltered
COPY CID-Synonym-unfiltered_1.csv /CID-Synonym-unfiltered/CID-Synonym-unfiltered_1.csv
COPY CID-Synonym-unfiltered_2.csv /CID-Synonym-unfiltered/CID-Synonym-unfiltered_2.csv
COPY CID-Synonym-unfiltered_3.csv /CID-Synonym-unfiltered/CID-Synonym-unfiltered_3.csv
RUN ls /CID-Synonym-unfiltered

RUN pwd
RUN mkdir /chunks
RUN python3 normalize.py
RUN ls /chunks && ls ..

CMD ["sh", "-c", "python3 populateTable.py $shared_directory"]