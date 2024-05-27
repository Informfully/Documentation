Google Play Store
=================

Before deploying the mobile app to the Google Play Store, the back end of the mobile app has to be deployed to a server.
For that, simply follow the same instructions as in `Back End Deployment <https://informfully.readthedocs.io/en/latest/deployment.html>`_.
Afterwards, make sure to change the ``SERVER`` constant in ``App.js`` (located `here <https://github.com/Informfully/Platform/blob/main/frontend/App.js>`_) to your server's address (e.g., ``wss://your.domain/websocket``).

What you need to prepare the release:

* Google Developer Account
* Android keystore
