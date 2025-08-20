User Creation
=============

User accounts for both the Mobile App and Administration Website are handled using Meteor's `Accounts system <https://docs.meteor.com/api/accounts.html>`_ and `password-based authentication <https://docs.meteor.com/api/passwords.html>`_.
All existing users are collected in the `users collection <https://informfully.readthedocs.io/en/latest/database.html>`_. 
There are two types of users: regular users (data field ``roles`` of collection ``users`` has a value ``user``) and admin users (data field ``roles`` of collection ``users`` has a value ``['user', 'admin']``).
Regular users can only access the Mobile App, whereas administrator users can access both the Mobile App and the Administration Website.

As we are using Meteor's default account and authentication system, there are currently two ways to create a new user.
You can do it either through the Administration Website or through the Mobile App.
Regular users can be created both through the Administration Website and the Mobile App, whereas admin users can currently be created only through the Mobile App.
The creation of user accounts through the Mobile App, however, is currently disabled (commented out in the source code).

Creation of Regular Users
-------------------------

Regular users are typically created over the tool for `User Creation <https://informfully.readthedocs.io/en/latest/experiment.html>`_, after a researcher has decided how many users will participate in the experiment.

Users can also create an account on their own via the app.
This feature, however, is currently disabled.
When creating experiments with this option enabled, we recommend that researchers create a survey for the group ``default-experiment``, where people need to submit their e-mail address.
This then allows for access control over the app.

Creation of Administrator Users
-------------------------------

Admin users are created manually by developers with access to the MongoDB. For that, a user account has to be created over the Mobile App, and consequently, its data fields in the user collection have to be manually overwritten. Specifically, the following fields have to be overwritten:

- ``roles``: needs to be changed from ``['user']`` to ``['user', 'admin']``
- ``participatesIn``: this is the experiment to which the Mobile App will be connected (if an admin user owns a couple of experiments, only one of them can be shown in the user's Mobile App). Currently, there is an 'admins-experiment', to which this field can be overwritten
- ``userGroup``: you can assign any group name to the admin user, e.g., DE, if you want to separate researchers according to the country of their university
- ``experiments`` (optional): this field does not have to be overwritten. You can use it to control which experiments an admin user owns, i.e., can see and manipulate, over the Admin Website. An experiment can be owned by multiple admin users. Be careful when allowing research access to other experiments
