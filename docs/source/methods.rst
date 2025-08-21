Meteor Methods
==============

Please see `Server Overview <https://informfully.readthedocs.io/en/latest/server.html>`_ for more information on the back end.

answers
-------

**answers.add**

* Adds a user's answers to a survey to the collection
* Input:

  * surveyId: ID of Survey
  * surveyAnswers: Array with answers to the survey

archive
-------

**archive.article.add**

* Add an article to the Favourites List of the current user
* Input:
  
  * articleId: ID of the article

**archive.article.remove**

* Remove an article from the Favourites List of the current user
* Input:
  
  * articleId: ID of the article

articleLikes/articleTotalLikes
------------------------------

**articleLikes.insert**

* Adds a statement of the current user for a particular article
* Adds the likes to the total likes of all users participating in the experiment
* Input:
  
  * articleId: ID of the article
  * articleQuestionId: Id of statement
  * experimentId: Id of the experiment the user participates in

**articleLikes.remove**

* Removes a statement like from the current user for a particular article
* Subtracts the likes from the total likes of all users participating in the experiment
* Input:

  * articleId: ID of the article
  * articleQuestionId: Id of statement
  * experimentId: Id of the experiment the user participates in

**articleDislikes.insert**

* Adds a statement of dislike from the current user for a particular article
* Adds the dislike to the total dislikes of all users participating in the experiment
* Input:

  * articleId: ID of the article
  * articleQuestionId: Id of statement
  * experimentId: Id of the experiment the user participates in

**articleDislikes.remove**

* Removes a statement dislike from the current user for a particular article
* Subtracts the dislike from the total dislikes of all users participating in the experiment
* Input:

  * articleId: ID of the article
  * articleQuestionId: Id of statement
  * experimentId: Id of the experiment the user participates in

articles
---------

**newsArticles.bookmark.update**

* Toggles the *bookmark* state of an article for a user
* Cycles between **in readingList** and **not in readingList**
* Uses methods _readingList.article.remove_ and _readingList.article.add_
* Input:

  * articleId: Id of the article

**newsArticles.favourite.update**

* Toggles the *favourite* state of an article for a user
* Cycles between **in favouritesList** and **not in favouritesList**
* Uses methods _archive.article.remove_ and _archive.article.add_
* Input:

  * articleId: ID of the article

articleViews
------------

**articleViews.add**

* Adds an additional article view for the current user
* Input:

  * articleId: ID of the article

**articleViews.duration.update**

* Adds time to the view duration of a particular article for the current user
* Input:

  * articleId: ID of the article

**articleViews.maxScrolledContent.update**

* Updates how much a user has scrolled down in a particular article, keeping the max value
* Input:

  * articleId: ID of the article
  * maxScrolledContent: A value between 0 and 1, showing how much of the article content has been seen by the user

experiments
-----------

**experiments.create**

* Creates a new experiment and assigns the new experiment to the user (who now owns the experiment)
* Input:

  * name: name of new experiment

**experiments.remove**

* Deletes and experiments from the database
* Input:

  * experimentId: ID of the experiment to remove

**experiments.update**

* Updates the name and launch status of an experiment
* Input:

  * experiment: experiment object

**experiments.launch**

* Launches an experiment (meaning some configurations cannot be changed anymore)
* Input:

  * experimentId: ID of the experiment

**experiments.likeSurvey.update**

* Updates the likeSurvey (now known as 'statements', shown after each article) of an experiment
* Input:

  * experimentId: ID of the experiment the likeSurvey belongs to
  * likeSurvey: likeSurvey object

**experiments.likeSurvey.remove**

* Removes the likeSurvey (statements) of an experiment
* Input:

  * experimentId: ID of the experiment the likeSurvey belongs to

**experiments.addUsers**

* Adds additional users to an experiment
* Input:

  * experimentId: ID of the experiment
  * amount: Number of new users
  * userGroup: Subgroup the users will be assigned

explanationViews
----------------

**explanationViews.insert**

* Adds a record in the database if a user has viewed the detailed recommendation explanations for an article
* Input:

  * articleId: ID of the article

pageViews
---------

**pageViews.add**

* Adds a page view of an article for a particular user
* Uses methods _articleViews.add_ and _articleViews.duration.update_
* Input:

  * page: name of page
  * previousPage: name of previous page
  * currentParameters: navigation parameters of the current page
  * prevParameters: navigation parameters of the previous page

podcastAnalytics
----------------

**podcastAnalytics.insert**

* Adds a record to the database of the type of action a user has performed when using the Audio player (including MiniPlayer)
* Input:

  * articleId: ID of the article
  * action: type of action performed by the user
  * podcastTimestamp: time in the audio player at which the action was performed

readingList
-----------

**readingList.article.add**

* Add an article to the Reading List of the current user
* Input:

  * articleId: ID of the article

**readingList.article.remove**

* Remove an article from the Reading List of the current user
* Input:

  * articleId: ID of the article

signins
-------

**signins.add**

* Add a sign-in log entry for the current user

surveys
-------

**surveys.create**

* Create a new survey
* Input:

  * surveyName: Name of new survey
  * experimentId: ID of the experiment the survey should belong to

**surveys.delete**

* Deletes a survey
* Input:

  * surveyId: Id of survey

**surveys.update**

* Updates the activity status of a particular survey
* Input:

  * surveyId: Id of survey
  * isActive: New active value

**surveys.questions.update**

* Updates the questions of a survey
* Input:

  * surveyId: Id of survey
  * surveyQuestions: Array of questions

users (default Meteor collection)
---------------------------------

**user.sendVerificationMail**

* Sends a verification email to the current user

**user.surveys.reset**

* Removes any answers to surveys for the current user

**user.remove**

* Deletes a specific user from the collection **users**
* Input:
  
  * userId: ID of the user

**user.savePushToken**

* Adds a notification token for the particular user in the database
* Input:
  
  * userId: ID of the user
  * pushToken: Notification token

videoAnalytics
--------------

**videoAnalytics.insert**

* Adds a record to the database of the type of action a user has performed when using the Video player
* Input:
  
  * articleId: ID of the article
  * action: type of action performed by the user
  * videoTimestamp: time in the video player at which the action was performed
