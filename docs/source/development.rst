Local Development
=================

This project was bootstrapped with `Create React Native App <https://github.com/react-community/create-react-native-app>`_.
This tutorial assumes basic knowledge of the React Native workflow for building apps.
It is not intended as a tutorial.
In case you need more information about React Native, the most recent version of this guide is available `here <https://github.com/expo/create-react-native-app/blob/master/README.md>`_.

Run a Local Server
--------------------------

Make sure that you are specifying the same port that you are using in the `React Native App <https://github.com/Informfully/Platform/blob/main/frontend/App.js>`_.
You can then start the server with:

.. code-block:: console

    # To run the server on port 3008 with
    # Settings configured for the development environment...
    ./meteor-start.sh

    # ...and...
    bash meteor-start.sh

    # ...or by specifying --port directly to run the server with
    meteor --port 3008 --settings settings-dev.json

If you want to access the server from within your network replace ``--port 3008`` with ``--port <YOUR_LOCAL_IP_ADDRESS>:3008``.
The back end is now running and the administration website is accessible at via ``localhost:3008``.

.. note::

    **Database Setup** You can connect to the database through ``mongodb://localhost:3009/`` if your Meteor server is running on port 3008.
    If the users collection in the database is empty when starting up, a new user with Maintainer role is created automatically by the genesis.js script <`Genesis script located here <https://informfully.readthedocs.io/en/latest/genesis.html>`_>.

You will need to install the following libraries and packages on your machine:

* `Meteor <https://docs.meteor.com/install.html>`_. The globally installed Meteor version does not matter, as the project will use the project-specific one defined in ``./backend/.meteor/release`` (`version note located here <https://github.com/Informfully/Platform/blob/main/backend/.meteor/release>`_, currently v2.14`_).
* XCode (macOS only) for iOS development and Android Studio for Android development.
* `Node.js <https://nodejs.org/>`_ Version **16**.
* `Yarn <https://classic.yarnpkg.com/lang/en/docs/install/>`_ Version **1.22 or higher**.
* `npm <https://docs.npmjs.com/downloading-and-installing-node-js-and-npm>`_ Version **8.1 or higher**.

To check whether you already have them installed, simply check the version in a terminal:

.. code-block:: console
    
    # Check whether Meteor installed and in PATH
    meteor --version

    # Check whether Node installed and in PATH
    node -v

    # Check whether npm installed and in PATH
    npm -v

    # Check whether yarn installed and in PATH
    yarn --version

Also, do not forget that it is best if your development and production environment have the same package versions (meaning that the libraries on the deployment server for the `website and back end <https://informfully.readthedocs.io/en/latest/deployment.html>`_ and `Docker container setup <https://informfully.readthedocs.io/en/latest/docker.html>`_ should also be updated).

Connecting to Local Server
--------------------------

Inside the ``App.js`` configuration file (`configuration file located here <https://github.com/Informfully/Platform/blob/main/frontend/App.js>`_), change the ``SERVER`` constant so it will connect to your local server.
E.g., if the client runs on the same computer:

.. code-block:: javascript

    const SERVER = 'localhost'

If you want to use your client on a different computer in the same network, replace ``localhost:3008`` with ``<YOUR_LOCAL_IP_ADDRESS>:3008``.

After you have set the ``SERVER`` constant, you can do the following to start the client:

.. code-block:: console

    # Go to front end directory
    cd frontend

    # Install all packages
    yarn install 

    # Start expo
    npx expo start

.. note::

    **Important** ``npx`` comes with ``npm`` and hence with ``Node.js``. ``npm`` will automatically fetch ``Expo``. If prompted, install ``npx`` and/or ``expo`` as required.

Afterwards, you can scan the QR code that will show up, if you want to test the app on a physical device (recommended).
Or you can connect to a device emulator (e.g., Android Studio or XCode).

.. image:: img/meteor_bundle.png
   :width: 700
   :alt: Screenshot of the Expo App

The app will run in the `Expo Go App <https://expo.dev/client>`_ and any changes to the source code will be automatically reflected in Expo Go.

Next Step: Platform Deployment
------------------------------

Please see the next instruction pages for `App Deployment <https://informfully.readthedocs.io/en/latest/native.html>`_ and `Website Deployment <https://informfully.readthedocs.io/en/latest/deployment.html>`_.
