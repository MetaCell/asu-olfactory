FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
      apt-get -y install sudo

USER root

# Update Ubuntu Software repository
RUN apt -y install python3-pip wget 
RUN pip install pandas psycopg2-binary wheel
RUN apt update
RUN dpkg --configure -a
RUN apt-get -y install -f git

WORKDIR $HOME/workspace
RUN ls
RUN git clone -b feature/20 https://github.com/MetaCell/asu-olfactory.git
RUN cd asu-olfactory && ls

WORKDIR $HOME/workspace/asu-olfactory
CMD [ "bash", "scripts/install.sh"]
