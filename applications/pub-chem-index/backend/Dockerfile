ARG CLOUDHARNESS_FLASK

FROM $CLOUDHARNESS_FLASK

ENV MODULE_NAME=pub_chem_index
ENV WORKERS=2
ENV PORT=8080
ENV BUILDDIR=/dist

COPY ./api-call-example-client ${BUILDDIR}
RUN ls -la
COPY requirements.txt /usr/src/app/

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev npm
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

WORKDIR /usr/src/app
RUN pip3 install -e .

RUN pwd && ls

WORKDIR ${BUILDDIR}
RUN npm install
RUN npm run build && cp -r build /usr/src/app/static && ls /usr/src/app
RUN cp -r build /usr/src/app/pub_chem_index/www && ls /usr/src/app/pub_chem_index/www

EXPOSE 8080
ENTRYPOINT gunicorn --log-level=info --preload --bind=0.0.0.0:8080 pub_chem_index.__main__:app
