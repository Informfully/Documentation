Back End Deployment (Website)
=============================

This project was bootstrapped with `Create React Native App <https://github.com/react-community/create-react-native-app>`_.
This tutorial assumes basic knowledge of the React Native workflow for building apps.
It is not intended as a tutorial.
In case you need more information about React Native, the most recent version of this guide is available `here <https://github.com/expo/create-react-native-app/blob/master/README.md>`_.

.. note::

    A valid SSL certificate for all communications between the front end and back end is required (as demanded by most recent Google and Apple storefront publishing guidelines).

Automatic Deployment
--------------------

For your convenience, we have created a script that automatically deploys the back end to the server.
To run it, simply execute the following
in a Terminal (with the current directory being the root of the back end repo):

.. code-block:: console

    # Deploy back end on the server
    bash build.sh

There are two scripts in the root directory of the project, `.snippets.sh` and `build.sh`.
You find the shell script ``build.sh`` in the back end folder (`shell script located here <https://github.com/Informfully/Platform/blob/main/backend/build.sh>`_).
Before the script can be used, the variables in the file ``.snippets.sh`` have to be set (`configuration file located here <https://github.com/Informfully/Platform/blob/main/backend/build.sh>`_).

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

The Administration Website can also be deployed using a generated Docker image.
To do that, simply follow the steps in the `Docker Setup <https://informfully.readthedocs.io/en/latest/docker.html>`_ for loading the image to the server.

Helper Scripts
--------------

Meteor encrypts all password of any users created using the `bcrypt <https://en.wikipedia.org/wiki/Bcrypt>`_ algorithm, which ensures that all passwords are encrypted a second time with an unknown "salt" value.
This protects against embarrassing password leaks in case the server’s database is compromised.

When a user logs in, the Meteor Account System checks the encrypted password generated with its "salt".
Trying to decrypt the salt is just as difficult to decrypt the password because of the nature of the bcrypt algorithm.
This special `encryption mechanism <https://docs.meteor.com/api/passwords>`_ employed by Meteor makes it impossible to insert a new user into the database without using Meteor.

Therefore, to createe the very first ``Maintainer``, we provide the main.js and genesis.js scripts that was run when the app starts up.
We connect (with ``main.js``) and check (with ``genesis.js``) if the database is empty and if yes, we insert a new user with the below user info (see again ``genesis.ja``).

**main.js**

.. code-block:: javascript

    //backend/server/main.js
    import { Meteor } from 'meteor/meteor';
    import '../imports/startup/server';
    import '../imports/api/server/publications';
    import './genesis'

    Meteor.startup(() => {

        if (process.env.MAIL_URL === undefined || process.env.MAIL_URL.length === 0) {
            process.env.MAIL_URL = 'smtp://localhost:25';
        }

    });

**genesis.js**

.. code-block:: javascript

    import { Accounts } from 'meteor/accounts-base'
    import { Meteor } from 'meteor/meteor';
    import '../imports/startup/server';

    
    if (Meteor.users.find().count() === 0) {

        const new_user = {
            "username": "[USERNAME]",
            "email": "[USERNAME]@[DOMAINN]",
            "password": "[PASSWORD]",
            "roles": [
                "user", "admin", "maintainer"
            ]   
        };

        Accounts.createUser(new_user);

        console.log("First user created");

    }

.. note::

    **Imporant** It is recommended to delete this user after other ``Maintainer`` has been created in order to ensure the safety of the system.
    This applied to both the local and online deployment of the back end.

Deploy Apps
-------------------------

Please see the other instruction page for `App Deployment <https://informfully.readthedocs.io/en/latest/native.html>`_
If you already have the apps up and running, go ahead and start your first `Use Experiment <https://informfully.readthedocs.io/en/latest/experiment.html>`_.
