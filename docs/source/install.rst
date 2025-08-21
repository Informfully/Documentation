Installation Instructions
=========================

This project was bootstrapped with `Create React Native App <https://github.com/react-community/create-react-native-app>`_.
This tutorial assumes basic knowledge of the React Native workflow for building apps.
It is not intended as a tutorial.
In case you need more information about React Native, the most recent version of this guide is available `here <https://github.com/expo/create-react-native-app/blob/master/README.md>`_.

.. _installation:

Download Codebase
-----------------

Informfully is a React Native app that uses a Meteor server as the back end. Download the code and Meteor as follows:

.. code-block:: console

    # Download the source code
    git clone https://github.com/Informfully/Platform.git

    # Install all packages
    cd backend
    meteor npm install

Here is an overview of the dependencies you need to install:

**Meteor** You do not have to install a specific version of Meteor.
When you run the application, Meteor will compare the version of the application with the version(s) you have installed locally.
If you are missing the application version, Meteor will automatically download and install the correct version for you.
Meteor and its command line tools are `available here <https://www.meteor.com/install>`_.

**Node** Meteor is shipped together with Node. 
You do not have to install it yourself.
If you want to deploy this application to production, however, a separate installation of Node will be required on the deployment server.

**NPM** Meteor comes with NPM and thus no manual installation is required.
Additionally, Meteor uses a bundled version of NPM that is available using ``meteor npm``.
In general, whenever you install, remove, or update packages for this project, you should use ``meteor npm`` instead of ``npm`` (e.g., ``meteor npm install`` to install dependencies).

**MongoDB** Meteor is shipped with MongoDB, and thus, you do not have to install it yourself.
If you still want to `install MongoDB yourself <https://docs.mongodb.com/manual/installation>`_, please check whether the version you want to install is compatible with the Meteor version this project uses in `.meteor/release <https://github.com/Informfully/Platform/blob/main/backend/.meteor/release>`_ to find the Meteor version of this project.

**Expo** You can use `Expo Go <https://expo.dev/go>`_ as an emulator to test your apps.
We recommend you download and use SDK47 to ensure full compatibility across all components.

Configuring Packager
--------------------

After downloading the code, you need to verify the React Native Packager Hostname. We have a brief guide for Mac, Linux, and Windows users.
When starting your project, you will see something similar to the following for your project URL:

.. code-block:: console
    
    exp://192.168.0.2:19000

The ``manifest`` at that URL tells the Expo app how to retrieve and load your app's JavaScript bundle, so even if you load it in the app via a URL like ``exp://localhost:19000``, the Expo client app will still try to retrieve your app at the IP address that the start script provides.
In some cases, this is less than ideal.

This might be the case if you need to run your project inside a virtual machine and you have to access the packager via a different IP address than the one that is printed by default.
In order to override the IP address or hostname that is detected by Create React Native App, you can specify your own hostname via the ``REACT_NATIVE_PACKAGER_HOSTNAME`` environment variable.

Mac and Linux:

.. code-block:: console

    REACT_NATIVE_PACKAGER_HOSTNAME='my-custom-ip-address-or-hostname' npm start

Windows:

.. code-block:: console

    set REACT_NATIVE_PACKAGER_HOSTNAME='my-custom-ip-address-or-hostname'
    npm start

The above example would cause the development server to listen on ``exp://my-custom-ip-address-or-hostname:19000``.

Informfully currently provides native Android and iOS apps. 
The Android APK can also be distributed outside Google Play.
It can be installed on Windows 11 and macOS (e.g., with third-party software like `BlueStacks <https://www.bluestacks.com/>`_).


Next Step: Run the Code
-------------------------

Please see the next instruction page for `Running the Code <https://informfully.readthedocs.io/en/latest/development.html>`_
