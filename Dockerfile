FROM acait/django-container:1.0.36 as app-prewebpack-container

USER root
RUN apt-get update && apt-get install mysql-client libmysqlclient-dev -y
USER acait

ADD --chown=acait:acait prereq_map/VERSION /app/prereq_map/
ADD --chown=acait:acait setup.py /app/
ADD --chown=acait:acait requirements.txt /app/

RUN . /app/bin/activate && pip install -r requirements.txt
RUN . /app/bin/activate && pip install mysqlclient

ADD --chown=acait:acait . /app/
ADD --chown=acait:acait docker/app_deploy.sh /scripts/app_deploy.sh
ADD --chown=acait:acait docker/app_start.sh /scripts/app_start.sh
ADD --chown=acait:acait docker/ project/
RUN chmod u+x /scripts/app_deploy.sh
RUN . /app/bin/activate && pip install django-webpack-loader


FROM node:8.16.0-jessie AS wpack
ADD . /app/
WORKDIR /app/
RUN npm install .
RUN npx webpack --mode=production

FROM app-prewebpack-container as app-container

COPY --chown=acait:acait --from=wpack /app/prereq_map/static/prereq_map/bundles/* /app/prereq_map/static/prereq_map/bundles/
COPY --chown=acait:acait --from=wpack /app/prereq_map/static/ /static/
COPY --chown=acait:acait --from=wpack /app/prereq_map/static/webpack-stats.json /app/prereq_map/static/webpack-stats.json

FROM acait/django-test-container:1.0.33 as app-test-container

COPY --from=app-container /app/ /app/
COPY --from=app-container /static/ /static/
