ARG CLOUDHARNESS_FLASK

FROM $CLOUDHARNESS_FLASK

ENV MODULE_NAME=pub_chem_index
ENV WORKERS=2
ENV PORT=8080
ENV BUILDDIR=/dist

COPY package.json ${BUILDDIR}/package.json
COPY package-lock.json ${BUILDDIR}/package-lock.json
COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

WORKDIR /usr/src/app
RUN ls -la
RUN pip3 install -e .


WORKDIR ${BUILDDIR}
RUN npm install
COPY ./api-call-example-client $BUILDDIR
RUN npm run build
COPY --from=base $BUILDDIR/build /usr/src/app/static


CMD python __main__