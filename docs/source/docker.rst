Docker Setup
============

Installation guide to set up Informfully using Docker containers for both the front end and back end.
The following are instructions to set up Docker containers for Informfully on Windows 10 Home.
A pre-requisite for Windows 10 Home users are to enable the WSL 2.0 feature.
WSL is the Windows Subsystem for Linux and the instructions for enabling it can be found `here <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_.
These instructions should work for Linux and MacOS as well.

To start from scratch, please download and install `Docker <https://www.docker.com/products/docker-desktop>`_.
Check if Docker has been set up by opening the command prompt/terminal (CMD on Windows) and type ``docker -v`` to check your docker version.
For this guide, Docker version 20.10.8 has been used.
Next is a step-by-step guide for building and loading a Docker image for both the front end as well as the back end.

Setting Up the Front End
------------------------

**Create Docker Image** ...

.. code-block:: python

    FROM node:16.13.0-alpine

    # IP adress of localhost
    ENV REACT_NATIVE_PACKAGER_HOSTNAME=192.168.0.12
    ENV EXPO_DEVTOOLS_LISTEN_ADDRESS=0.0.0.0

    EXPOSE 19000
    EXPOSE 19001
    EXPOSE 19002

    WORKDIR '/app'

    COPY package.json .
    COPY app.json .
    RUN npm install --global expo-cli
    RUN npm install --legacy-peer-deps
    COPY . .

    CMD ["expo", "start"]

**Build Docker Image** ...

**Run Docker Container** ...

**Save Docker Image** ...

**Load Docker Image** ...

**Troubleshooting** ...

Setting Up the Back End
-----------------------

**Create Docker Image** ...

.. code-block:: python

    # Configuration from phusion passenger docker, "https://github.com/phusion/passenger-docker"
    # Version 2.0.0 still has a Node version 14, which is compatible with the local Meteor Node version 12.
    # If you want to generate the Docker image with the latest Node version, you need to make sure that the
    # local Meteor Node version is compatible with it (or even better, it is the same)
    FROM phusion/passenger-nodejs:2.0.0
    # FROM phusion/passenger-nodejs
    ENV HOME /root
    CMD ["/sbin/my_init"]  

    # Install necessary tools
    RUN apt-get update \
    && apt-get install -y wget \
    && apt-get install -y sudo

    # Install MongoDB
    RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add - \
    && echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee 
    /etc/apt/sources.list.d/mongodb-org-4.4.list \
    && apt-get update
    RUN apt-get install -y mongodb \
    && sudo apt-get update

    # Our own configuration
    WORKDIR '/home/app/'
    COPY package.json .
    COPY Passengerfile.json .
    COPY . .

    # Install all dependencies of the bundle, similar to manual deployment (it uses the Node/NPM version of the Docker image)
    WORKDIR '/home/app/bundle/programs/server'
    RUN npm install --only=prod
    WORKDIR '/home/app/'

    # Make a database directory for MongoDB in the Docker image and change owner permissions for the directory to allow access
    RUN sudo mkdir -p /data/db
    RUN sudo chown `id -u` /data/db/

    CMD ["mongod"]

**Build Docker Image** To run the following commands, open Docker Desktop to start the Docker service (or use systemctl, etc. for Linux).
Navigate to the back end folder on the command line and type the command docker ``build . -t`` informfullybackend which will locate the Dockerfile in the current directory and execute all commands written on that file.

**Run Docker Container** ...

**Save Docker Image** ...

**Load Docker Image** ...

**Troubleshooting** ...
