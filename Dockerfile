FROM node:8.15.1-jessie AS wpack
ADD . /app/
WORKDIR /app/
RUN npm install .
RUN npx webpack

FROM acait/django-container:feature-refactor
RUN apt-get update && apt-get install mysql-client libmysqlclient-dev -y
ADD prereq_map/VERSION /app/prereq_map/
ADD setup.py /app/
ADD requirements.txt /app/
RUN . /app/bin/activate && pip install -r requirements.txt
ADD . /app/
ADD docker/app_start.sh /scripts/app_start.sh
USER acait
RUN . /app/bin/activate && pip install django-webpack-loader

CMD ["/scripts/start.sh" ]

COPY --from=wpack /app/prereq_map/static/prereq_map/bundles/* /app/prereq_map/static/prereq_map/bundles/
COPY --from=wpack /app/prereq_map/static/ /static/
COPY --from=wpack /app/prereq_map/static/webpack-stats.json /app/prereq_map/static/webpack-stats.json
