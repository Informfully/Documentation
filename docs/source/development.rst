Local Development
=================

This tutorial guides you through running the application with a local server for development and testing purposes.
There two seperate components that need to be set up, the **front end ** and the **back end**.
You will need to install the following libraries and packages on your machine

* `Meteor <https://docs.meteor.com/install.html>`_. The globally installed Meteor version does not matter, as the project will use the project-specific one defined in ``./backend/.meteor/release`` (currently 2.14).

* XCode (macOS only) for iOS development and Android Studio for Android development.
- `Node.js <https://nodejs.org/>`_ Version **16**.
- `Yarn <https://classic.yarnpkg.com/lang/en/docs/install/>`_ Version **1.22 or higher**.
- `npm <https://docs.npmjs.com/downloading-and-installing-node-js-and-npm>`_ Version **8.1 or higher**.

To check whether you already have them installed, simply check the version in a terminal:

.. code-block:: console
    
    # check whether Meteor installed and in PATH
    meteor --version

    # check whether Node installed and in PATH
    node -v

    # check whether npm installed and in PATH
    npm -v

    # check whether yarn installed and in PATH
    yarn --version

Also, do not forget that it is best if your development and production environment have the same package versions (meaning that the libraries on the deployment server for the `website and back end <https://informfully.readthedocs.io/en/latest/deployment.html>`_ and `Docker container setup <https://informfully.readthedocs.io/en/latest/docker.html>`_ should also be updated).

Running a Local Server
----------------------

...

Connecting to Local Server
--------------------------

Afterwards, you can scan the QR code that will show up, if you want to test the app on a physical device (recommended).
Or you can connect to a device emulator/simulator (e.g., Android Studio or XCode).

.. image:: img/meteor_bundler.png
   :width: 700
   :alt: Screenshot of the Expo App

The app will run in the `Expo Go App <https://expo.dev/client>`_ and any changes to the source code will be automatically reflected in Expo Go.
