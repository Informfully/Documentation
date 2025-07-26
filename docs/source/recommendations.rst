Recommendation Lists
====================

This page provides information on how to populate the ``recommendationLists`` `data collection <https://informfully.readthedocs.io/en/latest/database.html>`_ in the back end and based on `user and item data <https://informfully.readthedocs.io/en/latest/compass.html>`_.
The `relevant code <https://github.com/Informfully/Documentation/tree/main/sample>`_ is shared separately.
To forward item recommendations to the back end of Informfully, they must be in the JSON Recommendation Exchange Forat (JREX):

..
  ID (ObjectID): Unique Object ID used for indexing.
  userID (String): ID of the user.
  itemID (String): ID of the item.
  prediction (Double): Prediction score that determines the position of the item within the recommendation list. The higher the score, the further up the item is placed in the news feed. Precision, upper, and lower limits of the score can be customized.
  recommendationAlgorithm (String): Algorithm used to calculate the recommendation. Can optionally include an explanation of why this item was recommended.
  isPreview (Boolean): The front end can display (or feature) items in a preview mode (with the item text and image across the entire screen. Alternatively, items can be shown using a downsized image with a square aspect ratio and title-only.
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
     - The front end can display (or feature) items in a preview mode (with the item text and image across the entire screen. Alternatively, items can be shown using a downsized image with a square aspect ratio and title-only.
   * - ``createdAt``
     - Date
     - Timestamp that records when the item recommendation was created.

.. note::

  Please note that ``isPreview`` is an optional parameter.
  If it is not set, then the item will always be displayed in the preview mode. 
  I.e., with a small thumbnail and article title (unless it is the first item, then it has the full preview image with title and lead).

Below, you find a reference implementation of how, starting with item and user pools, such a JREX list of recommendations is created using the function ``create_recommendation()``.
The script will automatically export the results to a file.
This file can be copied/sent to the database.
Simply create a new document collection  ``recommendationLists`` and add the values of the recommendation file.

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

JREX allows you to add recommendations for a user.
Editing and updating recommendations are done by moving old recommendations to a separate archive collection (recommended) or by deleting them from the recommendation list.
The exact workflow is up to the researchers to define.
Different frameworks have different approaches.
Editing can be done via  `MongoDB Compass <https://informfully.readthedocs.io/en/latest/compass.html>`_. 
