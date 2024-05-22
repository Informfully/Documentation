Website Deployment
==================

To deploy the Admin Website without Docker, a build shell script ``build.sh`` back end folder (located `here <https://github.com/Informfully/Platform/blob/main/backend/build.sh>`_).
Before the script can be used, the variables in the file ``.snippets.sh`` have to be set (located `here <https://github.com/Informfully/Platform/blob/main/backend/build.sh>`_).
In short, the script will automate the following steps:

#.  Use the command ``meteor build`` to create the Node app bundle.
#.  Upload the bundle to the server using ``scp`` (the password of back end server will be required).
#.  SSH to remote machine (password required again).
#.  Unpack the tar.gz bundle created by using the ``build.sh`` script.
#.  Run ``npm install`` inside ``bundle/programs/server`` to install dependencies.
#.  Move the bundle folder to the ``/var/newsapp/`` location.
#.  Restart the Phusion Passenger process to serve the Node app.

Following these steps will deploy the new Administration Website.
For more details on the steps, you could also check the `back end deployment in the Quick Start Guide <https://informfully.readthedocs.io/en/latest/quick.html>`_.
This setup was succesfully tested on a server with the following software packages:

* Operating System: **Debian GNU/Linux 10 x86_64**
* Node Version: **14.18.1**
* NPM Version: **6.14.15**
* Phusion Passenger Version: **6.0.12**
* MongoDB Version: **4.4.3**

The Administration Website can also be deployed using a generated Docker image.
To do that, simply follow the steps in the `Docker Setup <https://informfully.readthedocs.io/en/latest/docker.html>`_ for loading the image to the server.
