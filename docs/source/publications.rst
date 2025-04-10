Meteor Publications
===================

See `Server Overview <https://informfully.readthedocs.io/en/latest/server.html>`_ for more information on the back end.


articleLikes
------------

* Publishes all currently active likes and dislikes by a user for a particular article, sorted by the creation date
* Arguments:
  
  * articleId: Id of article

articleTotalLikes
-----------------

* Publishes the total currently active likes and dislikes by the participants in an experiment for a particular article
* Arguments:

  * articleId: Id of article
  * experimentId: Id of experiment

articleViews
------------

* Publishes viewing information (like how many times the article has been opened) by a user for a particular article
* Arguments:

  * articleId: Id of article

experiments
-----------

* Publishes experiments that the user owns (assuming that the user is 'admin')

activeExperiment
----------------

* Publishes the experiment that the user takes part in (a user can take part in only one experiment)

newsArticles
------------

* Publishes all news articles in the database, sorted by datePublished

notification
------------

* Publication to check for new articles. Only publishes a single object at a time with the timestamp of the most current recommended article. If there are no recommendation, the newest timestamp of the newest article is published.

newsArticlesJoined
------------------

* Publishes the recommended articles for the user
* If there are no recommendations, returns the latest articles
* Reactive to changes regarding Reading List and Favourites List, i.e. it automatically updates their respective statuses
* Not reactive to newly added articles or recommendations!
* Arguments:

  * limit: Number of articles that should be returned
  * date: current date (variable not used in current implementation)

newsArticlesInReadingList
-------------------------

* Publishes news articles in the Reading List of the user, fully reactive

newsArticlesInArchive
---------------------

* Publishes news articles in the Favourites List of the user, fully reactive

furtherRecommendedNewsArticles
------------------------------

* Publishes news articles which have the same primaryCategory as the article with articleId
* Publishes either articles from Recommendations collection (sorted according to prediction score) or from newsArticles collection (sorted according to datePublished)
* Arguments:

  * limit: Number of articles that should be returned
  * primaryCategory: primaryCategory of the returned articles
  * articleId: the article for which the further recommendations are generated

surveys
-------

* Publishes surveys that are owned by the user

surveys.unanswered
------------------

* Publishes the surveys that the current user has not answered yet

userData
--------

* Publishes own roles, experiments (the user is admin of) and fullName for the current user

users.all
---------

* Publishes all users that the current user 'owns' (all users that participate in experiments that the current (admin) user owns)
