Back End Deployment (Website)
=============================

For your convenience, we have created a script that automatically deploys the back end to the server.
To run it, simply execute the following
in a Terminal (with the current directory being the root of the back end repo):

.. code-block:: console
    # Deploy back end on the server
    bash build.sh

There are two scripts in the root directory of the project, `.snippets.sh` and `build.sh`.
You find the shell script ``build.sh`` in the back end folder (located `here <https://github.com/Informfully/Platform/blob/main/backend/build.sh>`_).
Before the script can be used, the variables in the file ``.snippets.sh`` have to be set (located `here <https://github.com/Informfully/Platform/blob/main/backend/build.sh>`_).

**.snippets.sh** This is the configuration file.
In this file we store all variables used for deployment such as the app user,
the temporary directory, the app directory, etc.

**build.sh** This script builds the application and copies the bundle to the server. It also performs the tasks of extracting and
moving the bundle to the correct directories (as specified in ``.snippets.sh``).
The script will also install npm dependencies and restart the app.

In short, the script will automate the following steps:

#.  Use the command ``meteor build`` to create the Node app bundle.
#.  Upload the bundle to the server using ``scp`` (the password of back end server will be required).
#.  SSH to remote machine (password required again).
#.  Unpack the tar.gz bundle created by using the ``build.sh`` script.
#.  Run ``npm install`` inside ``bundle/programs/server`` to install dependencies.
#.  Move the bundle folder to the ``/var/newsapp/`` location.
#.  Restart the Phusion Passenger process to serve the Node app.

Following these steps will deploy the new Administration Website.
Please make sure to follow the instructions of the `Genesis Script <https://informfully.readthedocs.io/en/latest/docker.html>`_ to initialize the first users.

This setup was succesfully tested on a server with the following software packages:

* Operating System: **Debian GNU/Linux 10 x86_64**
* Node Version: **14.18.1**
* NPM Version: **6.14.15**
* Phusion Passenger Version: **6.0.12**
* MongoDB Version: **4.4.3**

Manual Deployment
-----------------

Please perform the following steps to deploy *an update* of the application.

**1. Build & Upload**

The following command will create a file called ``backend.tar.gz`` in the ``.build`` directory in the root of the project.

.. code-block:: console
    
    meteor build --server-only --architecture os.linux.x86_64 ./.build/

Next, you upload the `backend.tar.gz` file to the server:

.. code-block:: console

    # Make sure that you have access to the server's network
    scp ./.build/backend.tar.gz [USERNA]@[SERVER]:/home/[USER]/uploads/

**2. Move & Unpack**

Connect to the server via SSH and move the newly copied ``backend.tar.gz`` file to a temporary directory and extract its contents:

.. code-block:: console

    ssh [USERNAME]@[SERVER]
    cd /var/www/[USERNAME]/tmp
    mv /home/[USERNAME]/uploads/backend.tar.gz .
    tar xzf backend.tar.gz

**3. Update & Restart**

Install all dependencies:

.. code-block:: console

    # Still inside /var/www/[PROJECTNAME]/tmp/
    cd ./bundle/programs/server
    npm install --only=prod

Update the bundle and restart the app:

.. code-block:: console

    cd /var/www/[PROJECTNAME]/
    rm -rf bundle
    mv /var/www/[PROJECTNAME]/tmp/bundle /var/www/[PROJECTNAME]/bundle
    mv /var/www/[PROJECTNAME]/tmp/backend.tar.gz /var/www/[PROJECTNAME]/builds/

    # restart the app
    passenger-config restart-app /var/www/[PROJECTNAME]/

Docker Deployment
-----------------

The Administration Website can also be deployed using a generated Docker image.
To do that, simply follow the steps in the `Docker Setup <https://informfully.readthedocs.io/en/latest/docker.html>`_ for loading the image to the server.

Code Features
-------------

...

Environment Configuration
-------------------------

...

Helper Scripts
--------------

...

Deploy Apps
-------------------------

Please see the other instruction page for `App Deployment <https://informfully.readthedocs.io/en/latest/native.html>`_
