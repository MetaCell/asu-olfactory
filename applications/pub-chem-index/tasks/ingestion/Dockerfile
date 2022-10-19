ARG CLOUDHARNESS_BASE

FROM $CLOUDHARNESS_BASE

USER root

RUN pip install --upgrade pip
# Update Ubuntu Software repository
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
#wget pandas==1.4.2 psycopg2-binary==2.9.3 wheel==0.37.1 async_timeout aiopg asyncio

WORKDIR /
COPY . .
RUN ls -la
RUN chmod +x ingest.sh
CMD /ingest.sh
