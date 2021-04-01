# Prerequisite Course Map

[![Build Status](https://github.com/uw-it-aca/prereq-map/workflows/tests/badge.svg?branch=master)](https://github.com/uw-it-aca/prereq-map/actions)
[![Coverage Status](https://coveralls.io/repos/github/uw-it-aca/prereq-map/badge.svg?branch=master)](https://coveralls.io/github/uw-it-aca/prereq-map?branch=master)

System Requirements
-------------------
* Python (3+)
* Django (2+)
* Docker
* Node

Docker
------

1. Clone the repository

        $ git clone https://github.com/uw-it-aca/prereq-map
        $ cd prereq-map

2. Docker/Docker Compose is used to containerize your local build environment
    and deploy it to a local container so you can view your application. Docker
    is configured to build an empty 'project' and copy the settings files located
    in the 'docker' directory.

        $ docker-compose up

3. In the case that changes are made to the Dockerfile or docker-compose.yml file,
    you will need to rebuild the image. In this case, 'app' is the name of the
    Docker image for the Django project.

        $ docker-compose up --build

4. View your application

        Demo: http://localhost:8000/

Node (local for now)
------------

1. Install the node dependencies on your local machine (for now). This will create
   a local 'node_modules' directory.

        $ npm install

2. Start the webpack "watch mode". This will leave the webpack compiler running
   and compile bundles automatically when changes are made to the source files.
   You'll need to restart this command if you make changes to the webpack config.

        $ ./node_modules/.bin/webpack --config webpack.config.js --watch

