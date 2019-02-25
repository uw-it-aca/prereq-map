#FROM acait/django-container:python3
#RUN useradd aca
#ADD --chown=aca docker/web/start.sh /start.sh
#RUN chmod +x /start.sh
#RUN mkdir /app/logs
#RUN chown aca /app/logs
#ADD --chown=aca prereq_map/VERSION /app/prereq_map/
#ADD --chown=aca setup.py /app/
#ADD --chown=aca requirements.txt /app/
#RUN . /app/bin/activate && pip install -r requirements.txt
#ADD --chown=aca /docker/web/apache2.conf /tmp/apache2.conf
#RUN rm -rf /etc/apache2/sites-available/ && mkdir /etc/apache2/sites-available/ && \
#    rm -rf /etc/apache2/sites-enabled/ && mkdir /etc/apache2/sites-enabled/ && \
#    rm /etc/apache2/apache2.conf && \
#    cp /tmp/apache2.conf /etc/apache2/apache2.conf &&\
#    mkdir /etc/apache2/logs
#RUN chown aca /etc/apache2/logs
#ADD --chown=aca . /app/
#ENV DB sqlite3
#ADD docker /app/project/
#USER aca
#CMD ["/start.sh" ]



FROM python:3.6
ENV PYTHONUNBUFFERED 1

# copy contents of repo into an 'app' directory on container
ADD . /app
WORKDIR /app

# install python dependency packages (via setup.py) on container
RUN pip install -r requirements.txt

# move manage.py out of sampleproj to root directory so that django can start
COPY sampleproj/manage.py /app/manage.py