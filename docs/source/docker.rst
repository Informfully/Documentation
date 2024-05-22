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

This is the file that Docker uses to build the Docker image.
It gives instructions to Docker on how to build the image and what to include in the image.
To create a Dockerfile, open a text editor, such as Notepad on Windows, and type the following contents:

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

Explanation of the code:

* ``FROM node:16.13.0-alpine`` imports a light-weight Linux distribution called Alpine with the Node.js v16.13.0 environment. This sets a base OS for the image on which the following processes and commands will operate on. We chose Node.js v16.13.0 as this was the local version of Node.js that we used to develop (`see here <https://informfully.readthedocs.io/en/latest/development.html>`_.
* ``REACT_NATIVE_PACKAGER_HOSTNAME`` needs to be set equal to the ip address of the host machine, to which the iOS or Android phone will connect
* ``EXPO_DEVTOOLS_LISTEN_ADDRESS`` should be left as it is, it is an environment variable required for running the Expo server on the Docker container and connecting to it over the host machine
* ``EXPOSE 19000 19001 19002`` are the ports, used by Expo, which we have to expose to access the Docker container from the host machine
* ``WORKDIR '/app'`` sets the directory where the contents of the image will be inside of the Linux OS
* ``COPY package.json .`` and ``COPY app.json .`` copy the package.json and app.json files from the current local directory into the working directory on the Linux OS made above
* ``RUN npm install --global expo-cli`` tells Docker to execute the command line argument npm install --global expo-cli, which installs the Expo command line tool into the Docker image
* ``RUN npm install --legacy-peer-deps`` executes the command npm install with the option of ignoring legacy peer dependencies. This is an option that has to be turned on if using a Node version 7.0+, since the package.json dependencies were made using Node version 6.XX. This command will install all the required dependencies into the Docker image
* ``COPY . .`` copies the contents from the frontend directory into the Docker image
* ``CMD ["expo","start"]`` then executes the command line argument expo start to start the Expo server, after which a QR code is shown on the command prompt and users can access the Informfully application with Expo Go client on their iOS or Android phones

**Build Docker Image** To run the following commands, open Docker Desktop to start the Docker service (or use systemctl, etc. for Linux).
Navigate to the frontend folder on the command line and type the command ``docker build . -t informfullyfrontend`` which will locate the Dockerfile in the current directory and execute all commands written on that file.

**Run Docker Container** Once the Docker image is built, a Docker container of it can be run by typing the command ``docker run -p 19000:19000 -p 19001:19001 -p 19002:19002 informfullyfrontend``.
This will start a Docker container (and the Expo service will get started on it). The ``-p 19000:19000`` is used to open the port 19000 from the container to be used on the ``localhost:19000`` on the host computer.
To access the Informfully application on an iOS or Android phone, scan the QR code shown in the command prompt.

**Save Docker Image** To save the created Docker image, type in the command prompt ``docker save -o informfullyfrontend.tar informfullyfrontend``.

**Load Docker Image** Transfer the Docker image on your server, or where the Docker image needs to be opened, and ensure Docker is installed.
To open the image, start the Docker service and type the following command from the directory where the Docker image is located: ``docker load -i <path to image tar file>``.
Please note that it may take a few minutes to load the file and no progress bar will be shown in the command line.

.. note::

    **Troubleshooting** 

    ``Access is denied' error while building Docker image`` This might be caused either by a missing permissions problem or by the project path being too long.
    To solve it, we moved temporarily our whole frontend folder directly under the ``C:\`` directory.
    This resolver the issues for us and allowed us to successfully generate the backend Docker image.

    ``Cannot successfully connect phone to Expo service`` If a QR code has been generated, however the user is facing problems connecting to the running Meteor service on the container, make sure that
    
    #.  all antivirus programs on the host machine have been disabled,
    
    #.  the firewall on the host machine has been disabled,
    
    #.  the phone and the host machine share the same wireless network, and
    
    #.  the wireless network is public.

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

Explanation of the code:

* The first set of instructions takes the base image of phusion passenger from the Docker repository. This image is configured with Node.js. More information can be found `here <https://github.com/phusion/passenger-docker>`_.
* The next set of instructions are required to install the basic commands in order to download and configure the rest of the required software. Afterwards, MongoDB is installed.
* The next set of instructions creates a folder called app and it copies the backend folder contents onto the image.
* All dependencies of the bundle folder are installed, using the npm version of the base Docker image of phusion passenger.
* A directory is created called /data/db from which MongoDB retrieves its database. The ownership permissions of the directory are set so MongoDb can access it.
* Finally, the command ``mongod`` starts the MongoDB service.

**Build Docker Image** To run the following commands, open Docker Desktop to start the Docker service (or use systemctl, etc. for Linux).
Navigate to the back end folder on the command line and type the command docker ``build . -t`` informfullybackend which will locate the Dockerfile in the current directory and execute all commands written on that file.

**Run Docker Container** Once the Docker image is built, a Docker container of it can be run by typing the command ``docker run -p 8020:8080 informfullybackend``.
This will start a Docker container (and the MongoDB service will get started on it).
The ``-p 8020:8080`` is used to open the port 8080 from the container to be used on the ``localhost:8020`` on the host computer.
Follow the next steps to get the Backend running:

#.  Type ``docker ps`` to see which containers are running.

#.  Copy the container ID of the container that is running the back end.

#.  Type ``docker exec -it [containerID] sh``, this will open the container and you will be able to execute commands on it

#.  Run the command ``passenger start`` inside of the opened Docker container. This will start the phusion passenger service. The back end will be running now

In order to open the back end server, running on the container, from the host computer, open an internet browser and type ``localhost:8020`` (which is the host port that was defined above).
The passenger's port 8080 of the container can be changed by editing the ``Passengerfile.json`` in the backend directory.
Additionally, any other unused port can be used for the localhost (the left-hand side of ``-p 8020:8080``), instead of 8020.

**Save Docker Image** To save the created Docker image, type in the command prompt ``docker save -o informfullybackend.tar informfullybackend``.

**Load Docker Image** Transfer the Docker image on your server, or where the Docker image needs to be opened, and ensure Docker is installed.
To open the image, start the Docker service and type the following command from the directory where the Docker image is located: ``docker load -i <path to image tar file>``.
Please note that it may take a few minutes to load the file and no progress bar will be shown in the command line.

.. note::

    **Troubleshooting** 

    ``Access is denied' error while building Docker image`` See entry above in the front end section.

    ``Node fibers issues`` Once the Docker container is running and you try to start the phusion passenger server, there may be an error message regarding node fibers.
    This is most probably caused, because the Node.js version of Meteor, with which the bundle folder was generated, is different from the one in the Docker image, which the phusion passenger server uses.

    To solve this problem, you would have to upgrade the Meteor version of the project (by running ``meteor upgrade``) or using an older version of phusion passenger's base Docker image.
    In our case, we used an older version of phusion passenger's base Docker image, which supports Node.js v14.
