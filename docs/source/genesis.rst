Genesis Script
==============

Meteor encrypts all password of any users created using the `bcrypt <https://en.wikipedia.org/wiki/Bcrypt>`_ algorithm, which ensures that all passwords are encrypted a second time with an unknown "salt" value.
This protects against embarrassing password leaks in case the server’s database is compromised.
When a user logs in, the Meteor Account System checks the encrypted password generated with its "salt".
Trying to decrypt the salt is just as difficult to decrypt the password because of the nature of the bcrypt algorithm.
This special `encryption mechanism <https://docs.meteor.com/api/passwords>`_ employed by Meteor makes it impossible to insert a new user into the database who can log in to the Meteor Account System without using Meteor itself.

Therefore, to createe the very first ``Maintainer``, we provide the main.js and genesis.js scripts that was run when the app starts up.
We connect (with ``main.js``) and check (with ``genesis.js``) if the database is empty and if yes, we insert a new user with the below user info (see again ``genesis.ja``).

**main.js**

.. code-block:: javascript

    //backend/server/main.js
    import { Meteor } from 'meteor/meteor';
    import '../imports/startup/server';
    import '../imports/api/server/publications';
    import './genesis'

    Meteor.startup(() => {

        if (process.env.MAIL_URL === undefined || process.env.MAIL_URL.length === 0) {
            process.env.MAIL_URL = 'smtp://localhost:25';
        }

    });

**genesis.js**

.. code-block:: javascript

    import { Accounts } from 'meteor/accounts-base'
    import { Meteor } from 'meteor/meteor';
    import '../imports/startup/server';

    
    if (Meteor.users.find().count() === 0) {

        const new_user = {
            "username": "adam",
            "email": "adam@uzh.ch",
            "password": "password",
            "roles": [
                "user", "admin", "maintainer"
            ]   
        };

        Accounts.createUser(new_user);

        console.log("First user created");

    }

.. note::

    **Imporant** It is recommended to delete this user after other ``Maintainer`` has been created in order to ensure the safety of the system.
    This applied to both the local and online deployment of the back end.
