Installation Instructions
=========================

.. _installation:

Informfully is a React Native app that uses a Meteor servers as back end. Download the code and Meteor as follows:

.. code-block:: console

    # Download the source code
    git clone https://github.com/Informfully/Platform.git

    # Install all packages
    cd backend
    meteor npm install

Here is an overview of the dependencies you need to install:

**Meteor** You do not have to install a specific version of meteor.
When you run the application, Meteor will compare the version of the application with the version(s) you have installed locally.
If you are missing the application version, Meteor will automatically download and install the correct version for you.
Meteor and its command line tools are `available here <https://www.meteor.com/install>`_.

**Node** Meteor is shipped together with Node. 
You do not have to install it yourself.
If you want to deploy this application to production, however, a separate installation of Node will be required on the deployment server.

**NPM** Meteor comes with NPM and thus no manual installation is required.
Additionally, Meteor uses a bundled version of NPM that is available using ``meteor npm``.
In general, whenever you install, remove or update packages for this project, you should use ``meteor npm`` instead of ``npm`` (e.g., ``meteor npm install`` to install dependencies).

**MongoDB** Meteor is shipped with MongoDB and thus you do not have to install it yourself.
If you still want to `install MongoDB yourself <https://docs.mongodb.com/manual/installation/>`_, please check whether the version you want to install is compatible with the Meteor version this project uses in `.meteor/release <https://github.com/Informfully/Platform/blob/main/backend/.meteor/release>`_ to find the Meteor version of this project.

Environment Configuration
-------------------------

...

Helper Scripts
--------------

...

Next Stap: Run the Code
-------------------------

Please see the next instruction page for `Running the Code <https://informfully.readthedocs.io/en/latest/native.html>`_`Running the Code <https://informfully.readthedocs.io/en/latest/development.html>`_
