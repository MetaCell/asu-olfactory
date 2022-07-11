ARG CLOUDHARNESS_BASE

FROM $CLOUDHARNESS_BASE

USER root

# Update Ubuntu Software repository
RUN apt -y install python3-pip wget
RUN pip install pandas psycopg2-binary wheel

WORKDIR /
COPY . .
RUN ls -la
RUN chmod +x ingest.sh
CMD /ingest.sh