FROM python:3.9

RUN apt-get update && \
      apt-get -y install sudo

USER root

# Update Ubuntu Software repository
RUN apt -y install python3-pip wget
RUN pip install pandas psycopg2-binary wheel

WORKDIR /
COPY . .
RUN ls -la
RUN chmod +x lookup.py
RUN echo '${env_variable1}'
CMD python3 lookup.py ${env_variable1}