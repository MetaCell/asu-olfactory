ARG CLOUDHARNESS_BASE

FROM $CLOUDHARNESS_BASE

USER root

RUN pip install --upgrade pip
# Update Ubuntu Software repository
RUN pip install wget pandas psycopg2-binary wheel async_timeout dask aiopg asyncio

WORKDIR /
COPY . .
RUN ls -la
RUN chmod +x ingest.sh
CMD /ingest.sh