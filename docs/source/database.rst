Database Collections
====================

Overview of all collections that exist.
Can be accessed via MongoDB to run queries for recommender frameworks.
All collections marked with a \*-symbol collect data through the user's interactions with the app.

algorithms
----------

**Description** ...

...

answers*
--------

**Description** ...

...

archive*
--------

**Description** ...

...

articleLikes*
-------------

**Description** ...

...

articleTotalLikes*
------------------

**Description** ...

...

articleViews*
-------------

**Description** ...

...

articleViewsUpgrade*
--------------------

**Description** ...

...

experiments
-----------

**Description** ...

...

explanationViews*
-----------------

**Description** ...

...

explanations
------------

**Description** ...

...

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

pageViews*
----------

**Description** ...

...

podcastAnalytics*
-----------------

**Description** ...

...

readingList*
------------

**Description** ...

...

recommendationLists*
--------------------

**Description** ...

...

signins*
--------

**Description** ...

...

surveys
-------

**Description** ...

...

users*
------

**Description** ...

...

userGroups
----------

**Description** ...

...

videoAnalytics*
---------------

**Description** ...

...
