Source Code Overview
===================

The Informfully Platform combined both the app front end and website back end in one project.
To get a better overview of how to write and extend this platform, we provide here a short project overview.
The two parts we look at in more detail are the ``frontend``  and ``backend`` directories.

``frontend`` Directory
----------------------

The mobile app is based on `React Native <https://reactnative.dev/>`_, a JavaScript framework for developing native applications for iOS and Android, and `Expo <https://expo.dev/>`_, a set of tools built on top of React Native.
If you have no experience with React Native, it is recommended that you check out `Getting Started <https://reactnative.dev/docs/getting-started/>`_ and `Environment Setup <https://reactnative.dev/docs/environment-setup>`_.
To get a feel for the difference between React Native and Expo, take a look at the following `Stackoverflow post <https://stackoverflow.com/questions/39170622/what-is-the-difference-between-expo-and-react-native>`_.

React Native does not impose any strict folder structure.
Nevertheless, the structure of the frontend repo is heavily influenced by the default folder structure, which is generated when starting a new React Native project (using Expo CLI).
Here is a summary of the frontend repo folder structure:

.. code-block:: console

    .expo/
    android/
    assets/
    components/
    screens/
    ...
    config/
    index.js
    lib/
    i18n/
    meteorOffline/
    parameters/
    utils/
    node_modules/
    styles/
    .eslintrc.json
    App.js
    app.json
    index.js
    package.json
    package-lock.json
    ...

The ``assets`` folder contains all static assets required by the application such as fonts, icons and images.

The ``components`` folder contains all custom-built UI components.
The subfolder ``screens`` holds all the main screens that the user can navigate to such as the ``Home`` screen, ``SignIn`` screen, or ``Settings`` screen.
The components used by these screens are located in the respective subfolder.
For instance, the ``Survey`` screen (``components/screens/Survey.js``) makes use of a button component to display the possible answers to a question.
This button component can be found in the ``components/survey/`` folder.

The ``config`` folder accommodates a configuration file ``index.js`` which stores the URL of the General Terms & Conditions and the Data Protection Regulations.
This file can be used to define additional configuration options in the future.

The ``lib`` folder houses code for the internationalization (``i18n/``) and offline functionality (``meteorOffline/``) of the app as well as some utility functions (``utils/``) and additional parameters (``parameters/``).
The internationalization is implemented using the third party library ``react-native-i18n`` (`see here for more information <https://www.npmjs.com/package/react-native-i18n>`_).
It can be configured in the ``i18n.js`` file and additional languages can be added in the ``locales`` subfolder.
Currently, the app is fully translated in English, German and French.

All the third party packages are managed in the ``package.json`` file.
The Yarn Package manager is used to manage the dependencies.

The ``styles`` folder is where all the colours and fonts for the application are defined.
Storing all styles in a single location ensures style consistency across the app (e.g., all screens using the same font family) and allows for easy customization.
For example, the colours used in the app can simply be changed in the ``styles/variables/colors.js`` file.

The ``.eslintrc.json`` file manages the `ESLint <https://eslint.org/>`_ configuration.
ESLint is a linting utility which ensures consistent code style and better code quality.

The ``index.js`` denotes the entry point to the application, it is the file that is run when the application is launched.
In it, the App component, which is defined in the ``App.js`` file, is loaded.

Finally, ``app.json`` is a configuration file used by Expo.
It is the go-to place for configuring parts of the mobile app that do not belong in the code, like app name, icon or version number.
A full list of all available properties can be found in the `Expo documentation <https://docs.expo.dev/versions/latest/config/app/>`_.

``backend`` Directory
---------------------

The backend repo is based on `Meteor <https://www.meteor.com/>`_ with `React <https://reactjs.org/>`_.
It is highly encouraged to complete the following `Tutorial <https://react-tutorial.meteor.com/>`_, to get a better understanding of Meteor and how it can be used together with React (which is the framework used for the development of the admin website user interface) or React Native (which is the framework used for the development of the mobile app user interface).
The back end repo contains both the Meteor backend (``server``) and the React-based admin website (``client``).
Complete the abovementioned Tutorial to better understand why the backend repo is structured like it is. 
Below, a short overview of the structure is provided.

The Meteor framework is a JavaScript NodeJS backend solution which integrates well with React and React Native and ships with `MongoDB <https://www.mongodb.com/>`_.
It includes a very special approach to project directories and files.
There is a set of directory names that causes the framework to apply a predefined file load order and availability.
For instance, a file that is inside a directory called ``server`` can only be loaded on the server, i.e. the backend code.

Similarly, files that are inside a directory called ``startup`` are loaded during startup.
In the `Meteor documentation <https://guide.meteor.com/structure.html>`_, Meteor explains and suggests a very clean project structure that considers their special file load behaviour.
In the back end repo, we use the application structure as suggested by the Meteor documentation and have further separated the code semantically for different groups and types of components.
Furthermore, we very clearly distinguish between different layers and concepts inside the application.
Here is a summary of the backend repo structure: 

.. code-block:: console

    .build/
    .meteor/
    bundle/
    client/
    stylesheets/
        base/
        components/
        defaults/
        elements/
        ...
    main.js
    imports/
    api/
        client/
        server/
        ...
    lib/
    startup/
        client/
        server/
    ui/
        components/
        elements/
        layout/
        modules/
        pages/
        App.jsx
        ...
    node_modules/
    public/
    fonts/
    images/
    server/
    main.js
    ...
    tests/
    .eslintrc.json
    .snippets.sh
    build.sh
    ...
https://informfully.readthedocs.io/en/latest/deployment.html
The ``.build/`` directory is generated when running the ``build.sh`` script for the deployment of the `Administration Website <https://informfully.readthedocs.io/en/latest/deployment.html>`_.
It contains the ``tarball`` (more information `here <https://docs.meteor.com/commandline.html#meteorbuild>`_), after having run the ``meteor build`` command in the terminal.
The unpacked tarball is actually the ``bundle/`` folder, which is needed for building the backend repo `Docker Image <https://informfully.readthedocs.io/en/latest/docker.html>`_.

The ``.meteor/`` directory is also automatically generated when running Meteor locally and should not be manually changed.
It contains a local copy of a MongoDB instance.

The directories ``client/`` and ``server/`` in the root of the backend repo include all the code that needs to be available only in one of the environments.
In both directories, there is a file called ``main.js`` which imports files from the ``imports/`` directory and loads everything that is needed in the environment.
For the ``client/``, these are the routes that are available (i.e. the URLs).
For the ``server/``, these are the set of database collections, the publications as well as some configurations.
The configurations include so called fixtures as well as a configuration file for account management (e.g., signing in and registrations).
A fixture is a set of records that is inserted into the database in the case that the database is empty.
It is commonly used in software projects in which certain records need to be available for development (and possibly also in production).
In our case, this includes some news articles, a survey and an experiment.

On the client, stylesheets are bundled and loaded automatically.
Since they need not be available on the server, they reside in the ``client/`` directory.
There is a set of directories inside the directory ``client/stylesheets/`` to distinguish between different groups of stylesheets.
Examples of such groups are ``components``, ``elements``, ``layout``, and ``defaults`` such that ``components`` includes the stylesheets for components like the survey or an article, ``elements`` includes stylesheets for generic HTML elements like inputs, buttons and forms, ``layout`` includes stylesheets for different parts of the application like sections, titles and similar and ``defaults`` includes stylesheets of reusable elements like colours, fonts and media queries.

The ``imports/`` directory includes another very important segmentation.
It includes the directories ``api``, ``lib``, ``startup``, and ``ui``.
Inside ``api`` there are only files that make up the API of the server.
That is, it includes all publications, collections and methods.
Again, it is separated into directories for client/server and components or concerns.
The ``lib`` directory includes code that can be reused across the entire project and which is not specific to any of the environments.
It consists of utility functions such as splitting strings, constructing arrays, sorting arrays and similar.
Within the directory, the code is split again by components and concerns.

The ``startup`` directory includes all files, for each directory, that are needed during startup.
Particularly, there is an ``index.js`` for the server as well as the client that loads all files that are needed during startup.
This simplifies the startup process and allows us to load the ``index.js`` files into the ``main.js`` files and split the complexity.
The ``ui`` directory includes all React components that are used for the user interface of the admin website.
The directory includes a very similar structure to the one applied to the ``client/stylesheets/`` directory.
There are again different groups of components such as ``layouts``, ``elements``, and ``modules``.
Inside those directories, subdirectories for types of components were created, like ``survey``, ``articles``, and ``header``.

All the third party packages are managed in the ``package.json`` file.
From it, the ``package-lock.json`` file will be generated when running ``meteor npm install``, which fetches all the required packages and stores them in the ``node_modules`` folder.

For better code quality and consistency, the software project again includes an `ESLint <https://eslint.org/>`_ configuration (``.eslintrc.json``).
