Recommendation Lists
====================

This page provides information on how to populate the ``recommendationLists`` `data collection <https://informfully.readthedocs.io/en/latest/database.html>`_ in the back end and based on `user and item data <https://informfully.readthedocs.io/en/latest/compass.html>`_.
The `relevant code <https://github.com/Informfully/Documentation/tree/main/sample>`_ is shared separately.

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides an overview of all components.
  And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.

Informfully uses a JSON Recommendation Exchange Format (JREX) to visualize item recommendations.
JREX allows you to add recommendations for any user who contains any item in your document collection.
It allows for specifying the following properties of the recommendation list:

..
  ID (ObjectID): Unique Object ID used for indexing.
  userID (String): ID of the user.
  itemID (String): ID of the item.
  prediction (Double): Prediction score that determines the position of the item within the recommendation list. The higher the score, the further up the item is placed in the news feed. Precision, upper, and lower limits of the score can be customized.
  recommendationAlgorithm (String): Algorithm used to calculate the recommendation. Can optionally include an explanation of why this item was recommended.
  isPreview (Boolean): The front end can display (or feature) items in a preview mode (with the item text and image across the entire screen. Alternatively, items can be displayed using a downsized image with a square aspect ratio and a title-only option.
  createdAt (Date): Timestamp that records when the item recommendation was created.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - ObjectID
     - Unique Object ID used for indexing.
   * - ``userID``
     - String
     - ID of the user.
   * - ``itemID``
     - String
     - ID of the item.
   * - ``prediction``
     - Double
     - Prediction score that determines the position of the item within the recommendation list. The higher the score, the further up the item is placed in the news feed. Precision, upper- and lower limits of the score can be customized.
   * - ``recommendationAlgorithm``
     - String
     - Algorithm used to calculate the recommendation. Can optionally include an explanation of why this item was recommended.
   * - ``isPreview``
     - Boolean
     - If set to TRUE, the front end displays items in a preview mode (with the item text and image across the entire screen). If set to FALSE, items are displayed using a downsized image (with a square aspect ratio and title only).
   * - ``createdAt``
     - Date
     - Timestamp that records when the item recommendation was created.

Below, you find a reference implementation of how, starting with item and user pools, such a JREX list of recommendations is created using the function ``create_recommendation()``.
(If you are unfamiliar with MongoDB and how to retrieve user and item IDs, please see the `MongoDB tutorial page <https://informfully.readthedocs.io/en/latest/compass.html>`_ on how to retrieve them.)
Again, you can use the `reference implementation <https://github.com/Informfully/Documentation/tree/main/sample>`_ mentioned above to turn the user-item recommendations into JREX.

.. note::

  The app will automatically download all images associated with articles displayed in the news feed.
  We, therefore, recommend including URLs to downsized images.
  This enables faster loading of items and prevents potential server bottlenecks.  

.. code-block:: python

    # Sample script for generating recommendations
    import json
    from bson.objectid import ObjectId
    from datetime import datetime
    from bson import json_util

    # Create a JREX recommendation entry
    def create_recommendation(user_id, article_id, prediction_score, algorithm_id):

        jrex_entry = {
            # MongoDB ObjectID
            "_id": ObjectId(),
            "userId": user_id,
            "articleId": article_id,
            "recommendationAlgorithm": algorithm_id,
            "prediction": prediction_score,
            "createdAt": datetime.now()
        }

        return jrex_entry

    # Export articles to JSON
    def write_recommendations(recommendation_list):

        filename = "recommendation_list.json"
        
        jrex_list = json.dumps(
            recommendation_list, 
            default=json_util.default, 
            indent = 2)
        
        #print(jrex_list)

        try:
            with open(filename, "w") as outfile:
                outfile.write(jrex_list)
            print("Export complete.")

        except:
            print("Export failed.")
            pass

    # Create a recommendation for each user
    def assign_articles(user_pool, article_pool, algorithm_name):

        recommendation_list = []

        # Assign each user...
        for i in range(0, len(user_pool)):

            prediction_score = 1000

            # ...each article with...
            for j in range (0, len(article_pool)):
                
                # ...a default prediction score.
                prediction_score = prediction_score - j

                jrex_entry = create_recommendation(
                    user_pool[i], 
                    article_pool[j], 
                    prediction_score, 
                    algorithm_name)

                recommendation_list.append(jrex_entry)

        return(recommendation_list)

    # Create and export sample recommendations
    def main():

        user_pool = ["LTuEwG8JKq2wYoKcR", "9cwgrvWwwh7oGKHoC"]
        article_pool = ["65725f877b7cac9e81bb8271", "65725f877b7cac9e81bb8272"]
        
        algorithm_name = "Default Algorithm"

        # Create sample recommendations for all users
        recommendation_list = assign_articles(user_pool, article_pool, algorithm_name)

        # Export recommendation list to JSON
        write_recommendations(recommendation_list)

    # Run example
    main()

By default, the front end requires the output of this function to be stored in a document collection with the name ``recommendationLists``.
The name of the collection can be changed (`see codebase <https://github.com/Informfully/Platform/blob/main/backend/imports/api/recommendations.js>`_).

The workflow for managing the recommendation list is left open.
For example, updating recommendations for a given user can be done by simply inserting new recommendations with a higher prediction score.
This will preserve existing/old entries and move them to the bottom of the recommendation list.
Alternatively, all existing items for a given user can be removed before updating the list to ensure that only new items are displayed.
To preserve the recommendation history, this second approach would require moving old recommendations to a separate collection before each update.
