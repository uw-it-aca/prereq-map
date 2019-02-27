[![Build Status](https://travis-ci.org/uw-it-aca/prereq_map.svg?branch=master)](https://travis-ci.org/uw-it-aca/prereq_map)
# prereq-map
Prerequisite Course Map

System Requirements
-------------------
* Python (3+)
* Django (2+)
* Docker

Setup
-----

1. Clone the repository

        $ git clone https://github.com/uw-it-aca/prereq_map
        $ cd prereq_map

Node
----

2. Install the node dependencies for the React Demo.

        $ npm install

Webpack
-------

3. Start the webpack "watch mode". This will leave the webpack compiler running
   and compile bundles automatically when changes are made to the source files.
   You'll need to restart this command if you make changes to the webpack config.

        $ ./node_modules/.bin/webpack --config webpack.config.js --watch

Docker
------

4. Docker/Docker Compose is used to containerize your local build environment
    and deploy it to a local container so you can view your application. Docker
    is configured to build an empty 'project' and copy the settings files located
    in the 'docker' directory.

        $ docker-compose up

5. In the case that changes are made to the Dockerfile or docker-compose.yml file,
    you will need to rebuild the image. In this case, 'app' is the name of the
    Docker image for the Django project.

        $ docker-compose up --build
