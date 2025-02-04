Database Collections
====================

Overview of all document collections (database tables) that exist.
They can be accessed via MongoDB to run queries for recommender frameworks.
All collections marked with a \*-symbol collect data through the user's interactions with the app.

In the examples given below, Informfully is used as a news recommendation app.
Out of consistency (i.e., to be consistent with the use case of the other parts of the documentation), ``article`` is used instead of ``items``.
For example, this overview uses ``articleId`` as key attribute.
If Informfully is used in another capacity, all records labelled ``articleId`` can be simply renamed to ``itemId``.

.. note::

  Please visit the `Informfully Datasets Repository <https://github.com/Informfully/Datasets>`_. 
  For an example of quality of the data once it is exported and the corresponding `Dataset Documentation <https://informfully.readthedocs.io/en/latest/datasets.html>`_.
  And read the `MongoDB Compass Tutotrial <https://informfully.readthedocs.io/en/latest/compass.html>`_ for instructions of how to interface/connect with the database in the back end.

answers*
--------

**Description** Collects the survey results of all users.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``surveyId``
     - String
     - ID of survey.
   * - ``userId``
     - String
     - ID of user.
   * - ``answers``
     - Array of Objects
     - Answers of the user to all questions in the survey.
   * - ``createdAt``
     - Date
     - Time at which the data record was created.

An example of what the answer field could look like is shown below:

.. code-block:: json

    "answers":[
        {
            "questionId": "dbEZHPsNryzY24vgP",
            "questionText": "Soll der Staat Menschen in Armut stärker unterstützen (Ausbau der Sozialhilfe)?",
            "selections": [{
                "_id": "29NqGpYwaNwAQhTZw",
                "text": "Eher ja",
                "value": 0.75
            }]
        },
    ...
    ]

archive*
--------

**Description** Collects whether an article has been archived and whether it is a part of the user's favourites list.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``articleId``
     - String
     - ID of article.
   * - ``userId``
     - String
     - ID of user.
   * - ``articlePublishedDate``
     - Date
     - Date the article was published.
   * - ``createdAt``
     - Date
     - Time at which the data record was created.
   * - ``removedAt``
     - Date
     - Time at which the data record was removed.


articleLikes*
-------------

**Description** Collects the like/dislike status (current and historical) of the statements after an article.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``articleId``
     - String
     - ID of article.
   * - ``userId``
     - String
     - ID of user.
   * - ``articleQuestionId``
     - String
     - ID of statement, comes from the objects in the answers array of the ``likeSurvey``-field of an experiments collection data record.
   * - ``articleAnswer``
     - Integer
     - Can be either 1 or -1, 1 stands for a Like and -1 stands for a Dislike.
   * - ``createdAt``
     - Date
     - Time at which the data record was created.
   * - ``removedAt``
     - Date
     - Time at which the data record was removed.

articleTotalLikes*
------------------

**Description** The collection keeps track of the total likes/dislikes of the users in an experiment.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``articleId``
     - String
     - ID of article.
   * - ``experimentId``
     - String
     - ID of experiment.
   * - ``counts``
     - String
     - Contains the total likes/dislikes for each statement. For more information about how the array looks like, see below.
   * - ``questions``
     - Date
     - Contains the ids of statements for which at least one like/dislike has been given.

An example of what the answer field could look like is shown below:

.. code-block:: json

    "counts": [
        {
            "articleQuestionId": "u9CqoCRqG7LmiaKF3",
            "countLikes": 5,
            "countDislikes": 1,
        },
        {
            "articleQuestionId": "br7CRMr3YeZdRedDd",
            "countLikes": 0,
            "countDislikes": 2,
        }
    ]

articleViews*
-------------

**Description** Contains various information about all articles a user has accessed.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``articleId``
     - String
     - ID of article.
   * - ``userId``
     - String
     - ID of user.
   * - ``articlePublishedDate``
     - Date
     - Date the article was published (referred to as ``dateScraped`` of article).
   * - ``duration``
     - Integer
     - Duration in ms for which article was open.
   * - ``maxScrolledContent``
     - Double
     - Shows how much the user has seen from the article's content; can be between 0 and 1; a 0 indicates that the user has not scrolled down yet.
   * - ``updatedAt``
     - Date
     - Date on which article was last accessed in case it has been opened multiple times.
   * - ``views``
     - Integer
     - Number of times the article has been viewed by this user.
   * - ``createdAt``
     - Date
     - Time at which the data record was created.

experiments
-----------

**Description** The ``experiments`` collection contains information(``_id``, ``name``, etc.) about these experiments and surveys set by the admin.
The information can be modified on the ``Information`` page while ``likeSurvey`` can be set on the ``Feedback`` page.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``name``
     - String
     - Name of the experiment, which is first set at the creation of the experiment.
   * - ``adminName``
     - String
     - Name of the admin of this experiment; by default, it is the string before ``@`` of the creator's email.
   * - ``contactInfo``
     - String
     - Contact information of the admin of this experiment; by default, it is the creator's email.
   * - ``description``
     - String
     - Text description of the experiments.
   * - ``urlPP``
     - String
     - URL to the Privacy Policy.
   * - ``urlTC``
     - String
     - URL to the Terms and Conditions.
   * - ``testingPhase``
     - Boolean
     - Flag which indicates whether the experiment has launched or not. A true value means that the experiment has not launched yet. Once an experiment is launched, it cannot go back to the design phase, no additional users can be added, survey questions cannot be edited, and statements in Feedback surveys tab cannot be edited.
   * - ``likeSurvey``
     - Object
     - This field contains the statements that are shown after each article and users can like or dislike. For more information about how the object looks like, see below.
   * - ``feedbackEmail``
     - String
     - E-mail which is shown in the mobile app and users can contact in case of questions.
   * - ``explanationTagsDef``
     - Object
     - Contains objects which define the explanation tags used in the experiment. For more information about how the object looks like, see below.
   * - ``maxNrExplanationTags``
     - Integer
     - Limits the number of explanation tags that can be shown per article. Set to 0 in case you want to disable use of explanation tags for the experiment.
   * - ``maxCharacterExplanationTagShort``
     - Integer
     - Limits the number of characters that are shown inside the explanation tags of each article preview.
   * - ``maxNrFurtherRecArticles``
     - Integer
     - Limits the number of articles that are recommended at the end of the ``Article`` page/screen. Set to 0 in case you want to disable those recommendations.
   * - ``totalLikesDislikesEnabled``
     - Boolean
     - Controls whether the total likes/dislikes are shown on the Article page/screen. Set to False to hide the total likes/dislikes.
   * - ``previewTitleLineHeight``
     - Integer
     - Controls the number of lines that are used for the title of an article on the small article previews. It can be increased up to 3 in case that ``maxNrExplanationTags`` is set to 0.

An example of what the likeSurvey field could look like is shown below:

.. code-block:: json

    "likeSurvey": {
        "question": "Wieso mögen Sie den Artikel nicht?",
        "answers": [
            {
                "_id": "u9CqoCRqG7LmiaKF3",
                "text": "Ich stimme den Aussagen des Artikels nicht zu.",
                "value": 0
            },
            {
                "_id": "br7CRMr3YeZdRedDd",
                "text": "Ich mag den Schreibstil nicht.",
                "value": 0
            }
        ]
    }

An example of what the explanationTagsDef field could look like is shown below:

.. code-block:: json

    "explanationTagsDef": {
        "60feefd58bd1b5012ad6e689": {
            "_id": "60feefd58bd1b5012ad6e689",
            "textShort": "Int",
            "textLong": "Interests",
            "textColorLight": "#FFFFFF",
            "textColorDark": "#FFFFFF",
            "backgroundColorLight": "#44546A",
            "backgroundColorDark": "#44546A",
            "detailedExplanation": "Lorem ipsum dolor sit amet ..."
        },
        ...
    }

explanationViews*
-----------------

**Description** Whenever a user views the detailed recommendation explanations for an article, a record is created in the collection.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``articleId``
     - String
     - ID of article.
   * - ``userId``
     - String
     - ID of user.
   * - ``createdAt``
     - Date
     - Time at which the data record was created.

explanations
------------

**Description** Contains the recommendation explanation tags for each article and user.
See `Explainable Recommendations <https://github.com/Informfully/Explanations>`_ for how explanations are shown inside the app.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``articleId``
     - String
     - ID of article.
   * - ``userId``
     - String
     - ID of user.
   * - ``explanationTagsId``
     - Array of Strings
     - Contains the IDs of the explanation tags, which will be shown for this article and user. The possible explanation tag IDs are defined in the field ``explanationTagsDef``. The array can also be empty.

newsArticles
------------

**Description** Contains all the news articles that have been scraped and added to the database.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of article
   * - ``articleType``
     - String
     - Can be one of three: text, video, or podcast. Indicates whether the article contains a video, an audio, or only text.
   * - ``title``
     - String
     - Title of the article.
   * - ``lead``
     - String
     - Lead of the article.
   * - ``body``
     - Array of Objects
     - Contains the article text as paragraphs. The paragraphs are objects of the array and they have two properties: type (String) and text.
   * - ``url``
     - String
     - URL through which the article can be accessed.
   * - ``image``
     - String
     - Optional field, the URL to the cover image of the article.
   * - ``multimediaURL``
     - String
     - Contains a link to a video or audio file. The field should be set to null if empty. Should be consistent with the field ``articleType`` (meaning that if we have a text articleType, multimediaURL is set to null).
   * - ``multimediaDurationInMillis``
     - Integer
     - The length of the multimedia file (video or audio) in ms. Should be set to 1 if ``articleType`` is text.
   * - ``datePublished``
     - Date
     - Time at which the article was published on the news outlet's website.
   * - ``dateScraped``
     - Date
     - Time at which the article was scraped.
   * - ``dateUpdated``
     - Date
     - Outlets might update the article contents. Instead of creating a new article, the contents of the previous version are updated.
   * - ``dateDeleted``
     - Date
     - Optional field, we are sometimes asked by the outlets to remove articles. Instead of deleting them, we add a dateDeleted entry. Articles with this entry will not be shown.
   * - ``author``
     - String
     - Can also be a press agency or sponsored content. In case of multiple authors, separate them with a comma (,) symbol.
   * - ``outlet``
     - String
     - Current options include BLICK, NZZ, TAGI, SRF, WOZ, or WW.
   * - ``primaryCategory``
     - String
     - The categoriy of an item.
   * - ``subCategories``
     - Array of Strings
     - The sub-categories of an article. This information is not always provided.
   * - ``language``
     - String
     - Langauge code of the article (e.g., en-US, de-CH, etc.)

.. note::

    Be aware that Android devices can only handle websites secured by an SSL certificate (i.e., only HTTPS websites and no HTTP websites). 
    Therefore, data fields like URL or multimediaURL should only contain HTTPS websites.

pageViews*
----------

**Description** Collects all the pages/menus a user has accessed.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``userId``
     - String
     - ID of user.
   * - ``page``
     - String
     - Unique ID of each page/menu, e.g., ``Home`` for the home screen.
   * - ``previousPage``
     - String
     - Same as ``page``, simply for the previous one (allows to track how the user has navigated through the menus).
   * - ``parameters``
     - Object
     - Contains navigation parameters of the previous page (and sometimes of the current one), e.g., ``articleId``. It is empty if there are no parameters to pass (for example from ``Home`` to ``Settings``).
   * - ``createdAt``
     - Date
     - Time at which the data record was created.

podcastAnalytics*
-----------------

**Description** Collects all actions performed with an audio (including MiniPlayer).

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``articleId``
     - String
     - ID of article.
   * - ``userId``
     - String
     - ID of user.
   * - ``action``
     - String
     - The action performed at this step. Currently available: play/stop, backwards, fastforward, sliderSearchComplete, single-/doubleTapLeft, single-/doubleTapRight, heartbeat every 10 seconds, fullscreenExit/-activate.
   * - ``podcastTimestamp``
     - Integer
     - Position in ms in the podcast at which this action was performed.
   * - ``createdAt``
     - Date
     - Time at which the data record was created.

readingList*
------------

**Description** Collects whether an article has been read and whether it is a part of the user's bookmark list.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``articleId``
     - String
     - ID of article.
   * - ``userId``
     - String
     - ID of user.
   * - ``articlePublishedDate``
     - Date
     - Date the article was published.
   * - ``createdAt``
     - Date
     - Time at which data record was created.
   * - ``removedAt``
     - Date
     - Time at which data record was removed.

recommendationLists
--------------------

**Description** Collects that are shown on the home screen of a user in the exact ordering determined by the recommender system.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``articleId``
     - String
     - ID of article.
   * - ``userId``
     - String
     - ID of user.
   * - ``prediction``
     - Double
     - Value that indicated the position of the item in the list (the higher the value, the further up in the list; no pre-defined range exists, is up to the recommender system).
   * - ``recommendationAlgorithm``
     - String
     - Name of the algorithm used to create the recommendation (optional).
   * - ``isPreview``
     - Boolean
     - A flag which indicates whether the article should appear big on the screen with the title, lead, and image (if ``FALSE``, the feed will only show a thumbnail image and the title).
   * - ``createdAt``
     - Date
     - Time at which the data record was created.

An example of what the recommendations need to be formatted is shown below:

.. code-block:: json

    "recommendationLists": [
        {
            "_id": ObjectId("dbdwHPsadszY24vgP"),
            "userId": "ksgsouZYPvBA2GiQb",
            "articleId": "632aa0137143f66fb32c0d63",
            "prediction": 1000,
            "recommendationAlgorithm": "Test Algorithm 1",
            "isPreview": True,
            "createdAt": 2022-09-21T12:19:40.229+00:00
        },
        {
            "_id": ObjectId("dbEZHPsadszY24vgP"),
            "userId": "ksgsouZYPvBA2GiQb",
            "articleId": "632aa02f7143f66fb32c1125",
            "prediction": 1001,
            "recommendationAlgorithm": "Test Algorithm 1",
            "isPreview": False,
            "createdAt": 2022-09-21T12:19:41.229+00:00
        },
        ...
    ]

.. note::

    We provide an in-depth `recommendation list tutorial <https://informfully.readthedocs.io/en/latest/recommendations.html>`_ on how to connect your recommener framework and the Informfully back end with the `relevant code <https://github.com/Informfully/Documentation/tree/main/sample>`_.

signins*
--------

**Description** Collects all times a user has accessed the app.
A new record is added each time the user refreshes the browser tab.
Hence, a record might not reflect the actual timestamp at which a given user has signed in (meaning the action of initially signing in).
In return, for users that hardly ever sign out and hence hardly ever sign in, it (more) correctly reflects the last time the user has used the application.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``userId``
     - String
     - ID of user.
   * - ``createdAt``
     - Date
     - Time at which the data record was created.

An example of what the questions field could look like is shown below:

.. code-block:: json

    "questions": [
        {
            "_id": "dbEZHPsNryzY24vgP",
            "text": "Are you in favor of voting or higher social benefits?",
            "surveyId": "HKjXEn7cECXuqJig4",
            "minSelect": 1,
            "maxSelect": 1,
            "answers": [
                {
                    "_id": "RG8QYzfBZWn94SfpQ",
                    "text": "Yes",
                    "value": 1
                },
                {
                    "_id": "29NqGpYwaNwAQhTZw",
                    "text": "Rather yes",
                    "value": 0.75
                },
                {
                    "_id": "Z4tz763dMMkWPFrTd",
                    "text": "Rather no",
                    "value": 0.5
                },
                {
                    "_id": "NcMfsArhHXed8CSJR",
                    "text": "No",
                    "value": 0.25
                }
            ]
        },
        ...
    ]

surveys
-------

**Description** Contains all surveys that admin users have defined (and not deleted).

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``userId``
     - String
     - ID of user.
   * - ``experiment``
     - String
     - ID of experiment
   * - ``isActive``
     - Boolean
     - A flag which indicates whether the survey will be shown in the mobile app to participants in the experiment. A True means that the survey will be shown.
   * - ``questions``
     - Array of Objects
     - Contains all the questions in the survey. For more information about how the array looks like, see below.
   * - ``createdBy``
     - String
     - ID of user.
   * - ``createdAt``
     - Date
     - Time at which the data record was created.

users*
------

**Description** Stores information of Maintainers, Admins, and Users.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - `username```
     - String
     - Username required for user to log in; username field can still be manually added, simply for display purposes in the app.
   * - ``emails``
     - Arra of Strings
     - Only for maintainers.
   * - ``roles``
     - Array of Strings
     - An Array consists of all the access rights of this account. This Array can be one of the following three: ``{0:"user"}``, ``{0:"user",1:"admin"}``, or ``{0:"user",1:"admin",2:"maintainer"}``.
   * - ``profile``
     - Object
     - For Maintainers: ``{createdAccount:Integer,lastLogin:Time}``; for Admins: ``{maxUserAccount:Integer,createdAccount:Integer,plainTextInitialPassword:String,lastLogin:Time}``; for Users: ``Null``.
   * - ``participatesIn``
     - String
     - For ``Users``: the experiment ``_id`` that the user is in; for ``Maintainers`` and ``Admins``: ``default-experiment``.
   * - ``userGroup``
     - String
     - For ``Users``: the user group name that the user is in (only one group at each point in time); for ``Maintainers`` and ``Admins``: ``baseline``.
   * - ``experiments``
     - Array
     - For ``Maintainers`` and ``Admins``: the experiment ``_id`` that they own;fFor Users: ``Null``.
   * - ``createdBy``
     - String
     - ID of user.
   * - ``services``
     - Object
     - Meteor default field for login, contains the password hash (bcrypt) and the loginTokens. They are used for authentication purposes.
   * - ``services.password``
     - Object
     - Encrypted password.
   * - ``createdAt``
     - Date
     - Time at which the data record was created.

.. note::

    Regarding the ``plainTextInitialPassword``, when the account is initially created, a random ``plainTextInitialPassword`` is generated.
    This password is then sent to the administrators, who are strongly advised to change it as soon as possible.

userGroups
----------

**Description** This collection maps the _id, name, of a user group to an algorithm.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``experimentId``
     - String
     - Experiment ``_id`` that this user group belongs to.
   * - ``name``
     - String
     - Name of this user group.

videoAnalytics*
---------------

**Description** Collects all actions performed with a video.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of data record.
   * - ``articleId``
     - String
     - ID of article.
   * - ``userId``
     - String
     - ID of user.
   * - ``action``
     - String
     - The action performed at this step. Currently available: play/stop, backwards, fastforward, sliderSearchComplete, single-/doubleTapLeft, single-/doubleTapRight, heartbeat every 10 seconds, fullscreenExit/-activate.
   * - ``videoTimestamp``
     - Integer
     - Position in ms in the video at which this action was performed.
   * - ``createdAt``
     - Date
     - Time at which the data record was created.
