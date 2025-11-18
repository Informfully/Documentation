Google Play Store Deployment
============================

Before deploying the mobile app to the Google Play Store, the back end of the mobile app has to be deployed to a server.
For that, simply follow the same instructions as in `Back End Deployment <https://informfully.readthedocs.io/en/latest/deployment.html>`_.
Afterwards, make sure to change the ``SERVER`` constant in ``App.js`` (located `here <https://github.com/Informfully/Platform/blob/main/frontend/App.js>`_) to your server's address (e.g., ``wss://your.domain/websocket``).

Requirements
------------

* Google Developer Account
* Android Keystore

Building the App
----------------

We use Expo's bare workflow to generate native Android project code.
This allows the application to be further developed using the native tools, such as Android Studio.
Follow these steps to build an APK:

    #. Ensure that all changes are committed (e.g., that your working tree is clean).
    #. Navigate to the frontend folder on the command line.
    #. Type ``npm install`` in the command line.
    #. Type ``expo eject`` in the command line.
    #. Open the Android project with Android Studio.
    #. Configure the project.
    #. Open the AndroidManifest.xml file using the file browser in Android Studio and add/remove permissions (see below for more details).
    #. Build -> Generate Signed Bundle/APK -> APK -> Give the key store path and enter credentials -> Release with both V1 (JAR Signature) and V2 (Full APK Signature) -> Finish.
    #. The APK will be generated in ``/android/app/release/app-release.apk``.

We used the following to successfully deploy to the Play Store. In case you have errors, try using the same versions:

* Operating System: **Windows 10**
* Android Studio: **4.2.2**
* Android Gradle Plugin Version: **3.5.3**
* Gradle Version: **6.3**
