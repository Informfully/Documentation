Front End Deployment (App)
===========================

This project was bootstrapped with `Create React Native App <https://github.com/react-community/create-react-native-app>`_.
This tutorial assumes basic knowledge of the React Native workflow for building apps.
It is not intended as a tutorial.
In case you need more information about React Native, the most recent version of this guide is available `here <https://github.com/expo/create-react-native-app/blob/master/README.md>`_.

App Preview
-----------

Test versions are available for free download if you only want to preview the app. 
Reach out to us to get a demo account: info@informfully.ch

* `Google Play Store (for Android devices, version 5.1 and newer) <https://play.google.com/store/apps/details?id=ch.uzh.ifi.news>`_

* `Apple App Store (for iOS devices, version 13.0 and newer) <https://apps.apple.com/ch/app/ddis-news/id1460234202>`_

.. note::

    Theoretically, the mobile app should be compatible with devices running iOS 11.0.
    However, `TestFlight <https://developer.apple.com/testflight/>`_ (which was used for testing the beta version of the app) is only supported by devices with a minimum iOS 13.0.
    Therefore, we were unable to test whether the mobile app is actually compatible with iOS 11.0.

Environment Setup
----------------

To build a release of the app, this tutorial assumes that you have already completed the previous steps.
If not, make sure to install everything listed in the `Installation Instructions <https://informfully.readthedocs.io/en/latest/install.html>`_.

You should only need to update the global installation of ``create-react-native-app`` very rarely, ideally never.
Upgrading to a new version of React Native requires updating the ``react-native``, ``react``, and ``expo`` package versions.
Ensure that the upgraded package versions are compatible with each other.

As explained in `Local Development <https://informfully.readthedocs.io/en/latest/development.html>`_, make sure to properly configure ``App.js`` in the ``frontend`` folder (`file here <https://github.com/Informfully/Platform/blob/main/frontend/App.js>`_).
Change the' SERVER' constant so that it connects to your local server.
If you do not apply these changes, then the app front end will not know what server to connect to.

You can edit ``app.json`` to include `configuration keys <https://docs.expo.io/versions/latest/guides/configuration.html>`_ under the ``expo`` key.
To change your app's display name, set the ``expo.name`` key in ``app.json`` to an appropriate string.
To set an app icon, set the `expo.icon` key in `app.json` to be either a local path or a URL.
It's recommended that you use a 512x512 PNG file with transparency.

Building Release
----------------

Create React Native App does a lot of work to make app setup and development simple and straightforward, but it is very difficult to do the same for deploying to Apple's App Store or Google's Play Store without relying on a hosted service.
We therefore recommend publishing to Expo's React Native Community.

Expo provides free hosting for the JS-only apps created by CRNA, allowing you to share your app through the Expo client app. This requires registration for an Expo account.
Install the ``exp`` command-line tool and run the publish command:

.. code-block:: console

    $ npm i -g exp
    $ exp publish

When it comes to building an Expo stand-alone app, you can also use a service like `Expo's standalone builds <https://docs.expo.io/versions/latest/guides/building-standalone-apps.html>`_ if you want to get an IPA/APK for distribution without having to build the native code yourself.

And if you want to build and deploy your app yourself, you will need to eject from CRNA and use Xcode and Android Studio.
This is usually as simple as running ``npm run eject`` in your project, which will guide you through the process.
Make sure to install ``react-native-cli`` and follow the `native code getting started guide for React Native <https://reactnative.dev/docs/getting-started>`_.

If you have made use of Expo APIs while working on your project, then those API calls will stop working if you eject to a regular React Native project.
If you want to continue using those APIs, you can eject to "React Native + ExpoKit" which will still allow you to build your own native code and continue using the Expo APIs
See the `ejecting guide <https://docs.expo.dev/expokit/eject/>`_ for more details about this option.

Once these steps have been completed, you are ready to create your first release.
We have more detailed instructions for `Android released <https://informfully.readthedocs.io/en/latest/google.html>`_ and `iOS releases <https://informfully.readthedocs.io/en/latest/apple.html>`_.

Helper Scripts
--------------

If Yarn was installed when the project was initialized, then dependencies will have been installed via Yarn, and you should probably use it to run these commands as well.
Unlike dependency installation, the command syntax for running commands is identical for Yarn and NPM at the time of this writing.

.. code-block:: console

    npm start

Runs your app in development mode.
Open it in the `Expo app <https://expo.io>`_ on your phone to view it.
It will reload if you save edits to your files, and you will see build errors and logs in the terminal.

.. code-block:: console
    
    npm test

Runs the `jest <https://github.com/facebook/jest>`_ test runner on your tests.

.. code-block:: console

    npm run ios

Like ``npm start``, but also attempts to open your app in the iOS Simulator if you're on a Mac and have it installed.

.. code-block:: console

    npm run android

Like ``npm start``, but also attempts to open your app on a connected Android device or emulator.
Requires an installation of Android build tools (see `React Native Documentation <https://reactnative.dev/docs/environment-setup>`_ for detailed setup).

.. code-block:: console

    npm run eject

This will start the process of "ejecting" from Create React Native App's build scripts.
You will be asked a couple of questions about how you'd like to build your project.

.. note::

    Running eject is a permanent action (aside from whatever version control system you use).
    An ejected app will require you to have an `XCode and/or Android Studio environment <https://reactnative.dev/docs/environment-setup>`_) set up.

Deploy Website
-------------------------

Please see the other instruction page for `Website Deployment <https://informfully.readthedocs.io/en/latest/deployment.html>`_.
If you already have the website up and running, go ahead and start your first `Use Experiment <https://informfully.readthedocs.io/en/latest/experiment.html>`_.
