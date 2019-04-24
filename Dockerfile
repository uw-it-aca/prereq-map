FROM node:8.15.1-jessie AS wpack
ADD . /app/
WORKDIR /app/
RUN npm install .
RUN npx webpack

FROM prereq-map_app
COPY --from=wpack /app/prereq_map/static/prereq_map/bundles/* /app/prereq_map/static/prereq_map/bundles/
COPY --from=wpack /app/prereq_map/static/ /static/
COPY --from=wpack /app/prereq_map/static/webpack-stats.json /app/prereq_map/static/webpack-stats.json
