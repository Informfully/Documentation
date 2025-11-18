Database Tutorial
=================

This page provides an introduction to retrieving user and item IDs from the MongoDB back end of Informfully for creating recommendation lists.
In the example shown on this page, we use `MongoDB Compass <https://www.mongodb.com/products/tools/compass>`_ to explore the database and its collections.
(In the context of MongoDB a "table" in the database is referred to as "collection" and "entry/tupel" as "document" instead.)

To customize the recommendations displayed to users, you must edit the following collections: ``users``, ``items``, and ``recommendations``, outlined below.
Customization of recommendation list entries is done using three steps:
* Create user accounts and retrieve their IDs
* Scrape/upload items to recommend and retrieve their IDs
* Create item recommendation lists for users

Retrieving User IDs
-------------------

.. image:: img/database_screenshots/collection_users.png
   :width: 720
   :alt: Home screen

``users`` collection:
The first step in creating a recommendation requires extracting User IDs.
In the user collection, you can filter by e-mail address or creation date.
This allows you to retrieve the ObjectIDs of the users you have created on the `website earlier <https://informfully.readthedocs.io/en/latest/items.html>`_.
Export the users and save the IDs.
We recommend you either create a custom mapping between the back end IDs and your external recommender framework or use the ObjectIDs in your framework as well.

Retrieving Item IDs
-------------------

.. image:: img/database_screenshots/collection_items.png
   :width: 720
   :alt: Home screen

``items`` collection:
Retrieving item IDs is identical to user IDs.
Simply export the IDs you need from this collection.
Ensure that both the back end and your recommender framework use the same IDs when generating user-specific recommendation lists.

.. note::

  Please visit the `Item Entries <https://informfully.readthedocs.io/en/latest/items.html>`_ page to see how Informfully stores recommendations.
  We provide an example of a news article entry.
  The collection, however, can accommodate any item and be configured to match your use case.

Creating Recommendation Lists
-----------------------------

.. image:: img/database_screenshots/collection_recommendations.png
   :width: 720
   :alt: Home screen

``recommendationLists`` collection:
The final step in creating custom recommendations is to combine user IDs and item IDs.
You can add entries 1) manually via MongoDB Compass, 2) import them via the interface, or 3) add them using a script.

.. note::

  Please visit the `Item Visualization <https://informfully.readthedocs.io/en/latest/recommendations.html>`_ page to see how you can create custom entries and forward recommendations from your external system.
