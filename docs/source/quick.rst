Quick Start Guide
=================

Find below the install instructions for both the front end and back end.


.. _installation:

Instllation Instructions
------------------------

Download **Informfully Platform** repository to start your journey:

.. code-block:: console

    # Download the source code
    git clone https://gitlab.ifi.uzh.ch/ddis/Students/Projects/2021-multimedia-news-recommendations.git

    # Install all packages
    cd backend
    meteor npm install

Informfully is a React Native app that uses a Meteor servers as back end. Here is an overview of the dependencies you need to install:

**Meteor** You do not have to install a specific version of meteor.
When you run the application, Meteor will compare the version of the application with the version(s) you have installed locally.
If you are missing the application version, Meteor will automatically download and install the correct version for you.
Meteor and its command line tools are `available here <https://www.meteor.com/install>`_.

**Node** Meteor is shipped together with Node. 
You do not have to install it yourself.
If you want to deploy this application to production, however, a separate installation of Node will be required on the deployment server.

**NPM** Meteor comes with NPM and thus no manual installation is required.
Additionally, Meteor uses a bundled version of NPM that is available using ``meteor npm``.
In general, whenever you install, remove or update packages for this project, you should use ``meteor npm`` instead of ``npm`` (e.g. ``meteor npm install`` to install dependencies).

**MongoDB**

For developing the app, you can chose between connecting to a local back end on your machine or a server.
Please see the instruction on the pages for `the local deployment <https://informfully.readthedocs.io/en/latest/development.html>`_ and `online deployment <https://informfully.readthedocs.io/en/latest/deployment.html>`_ respectively.

Helper Scripts
--------------

...
