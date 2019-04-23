FROM node:8.15.1-jessie AS wpack
ADD . /app/
WORKDIR /app/
RUN npm install .
RUN npx webpack
RUN ls /app/prereq_map/static

FROM acait/django-container:develop
RUN apt-get update && apt-get install mysql-client -y
RUN mkdir /app/logs
ADD prereq_map/VERSION /app/prereq_map/
ADD setup.py /app/
ADD requirements.txt /app/
ENV LC_ALL C.UTF-8
RUN . /app/bin/activate && pip install -r requirements.txt
ADD /docker/web/apache2.conf /tmp/apache2.conf
RUN rm -rf /etc/apache2/sites-available/ && \
    mkdir /etc/apache2/sites-available/ && \
    rm -rf /etc/apache2/sites-enabled/ && \
    mkdir /etc/apache2/sites-enabled/ && \
    rm /etc/apache2/apache2.conf && \
    cp /tmp/apache2.conf /etc/apache2/apache2.conf && \
    mkdir /etc/apache2/logs
ADD . /app/
ENV DB sqlite3
ADD docker /app/project/
ADD docker/web/start.sh /start.sh
RUN chmod +x /start.sh
RUN mkdir /static

RUN groupadd -r prereq_map -g 1000 && \
    useradd -u 1000 -rm -g prereq_map -d /home/prereq_map -s /bin/bash -c "container user" prereq_map &&\
    chown -R prereq_map:prereq_map /app &&\
    chown -R prereq_map:prereq_map /static &&\
    chown -R prereq_map:prereq_map /var &&\
    chown -R prereq_map:prereq_map /run &&\
    mkdir /var/lock/apache2 &&\
    chown -R prereq_map:prereq_map /var/lock/ &&\
    chown -R prereq_map:prereq_map /home/prereq_map
USER prereq_map

COPY --from=wpack /app/prereq_map/static/prereq_map/bundles/* /app/prereq_map/static/prereq_map/bundles/
COPY --from=wpack /app/prereq_map/static/ /static/
COPY --from=wpack /app/prereq_map/static/webpack-stats.json /app/prereq_map/static/webpack-stats.json

RUN ls /app/prereq_map/static

RUN . /app/bin/activate && pip install django-webpack-loader

ENV PORT 8000
CMD ["/start.sh" ]
