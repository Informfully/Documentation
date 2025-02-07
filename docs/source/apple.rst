Apple App Store Deployment
==========================

Before deploying the mobile app to the Apple App Store, the back end of the mobile app has to be deployed to a server.
For that, simply follow the same instructions as in `Back End Deployment <https://informfully.readthedocs.io/en/latest/deployment.html>`_.
Afterwards, make sure to change the ``SERVER`` constant in ``App.js`` (located `here <https://github.com/Informfully/Platform/blob/main/frontend/App.js>`_) to your server's address (e.g., ``wss://your.domain/websocket``).

Requirements
------------

* Apple Developer Account and Apple device with Xcode
* iPhone distribution certificate

Building the App
----------------

Navigate to the frontend folder on the command line.
Run the following command on a clean working branch to create the temporary iOS project.
We will discard all changes after uploading the iOS app/testing the iOS app.

.. code-block:: console

    # Install node modules
    npm install
    
    # Switch from Expo's managed workflow to the bare workflow
    expo eject

We used the following to successfully deploy to the App Store. In case you have errors, try using the same versions:

* Operating System: **macOS Big Sur Version 11.6**
* Xcode: **13.0**
* Yarn: **1.22.11**
* Watchman: **2021.09.13**
