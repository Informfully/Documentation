Experiment Setup
================

Launching an experiment assumes you already have the apps published, the website launched, and the back end server running.
If this is not the case, please go back to the `Installation Instructions <https://informfully.readthedocs.io/en/latest/install.html>`_ and follow the tutorial step-by-step.

The following guidelines provide a detailed overview of how to set up and configure such experiments.
A sample experiment of launching Informfully as a news recommendation platform will be used as an example to guide through each of the experiment's phases.

.. note::

   Please see the `Experiment Overview <https://informfully.readthedocs.io/en/latest/overview.html>`_ to get a high-level overview of how the components outlined below interact during a user experiment.

.. _setup:

Create Experiment
-----------------

The ``Experiments`` screen is where you manage your experiments.
You can create multiple experiments and run them simultaneously with completely separate participants and surveys.

To create a new experiment, click on the ``NEW EXPERIMENT``-button.
An overlay with a form will appear, allowing you to enter a name for the new experiment.
After pressing ``CREATE EXPERIMENT``, you will see the new experiment on the screen.
On the right, the name can be changed by editing the text field and clicking the ``SAVE CHANGES``-button.

The initial experiment status is ``DESIGN``.
At this stage, the administrator can add users, modify surveys, and experiment with the setup.
Once the status is switched to ``LAUNCHED`` by clicking the button, the experiment settings are locked to preserve the integrity of the results.

Select or deselect an experiment by clicking on the large button on the left.
Once an experiment has been selected, the tabs in the top menu bar are revealed (the menu may be hidden behind a menu icon on smaller screens).
The tabs in the top menu bar are described in the subsections below.

.. image:: img/tutorial_screenshots/tutorial_1.jpg
   :width: 700
   :alt: Experiments screen

.. _users:

Create Users
------------

Once an experiment is selected in the ``Experiments`` screen, the participants of that experiment will be listed on the ``Users`` screen.
Find out more about `User Creation <https://informfully.readthedocs.io/en/latest/users.html>`_.

If the experiment is new, new users can be added by pressing ``ADD USERS``. 
Another module will appear with a form, where the user amount and the user group can be specified.
The user group can be any text to discern participants into groups (e.g. ``baseline`` and ``experimental``).
After submitting, users should immediately appear in the list.
New users are created with randomly generated usernames and passwords.
The passwords can be accessed by exporting a CSV file by pressing the ``CSV EXPORT``-button.
A download prompt will pop up.

.. image:: img/tutorial_screenshots/tutorial_2.jpg
   :width: 700
   :alt: User screen


Each individual user can be deleted by clicking the trash can on the right of the row.
We recommend exporting the user accounts as a CSV file and creating a backup copy.
(E.g., for support purposes, in case users forget their password.)

.. _surveys:

Create Surveys
--------------

Informfully has a built-in `Survey Tool <https://informfully.readthedocs.io/en/latest/surveys.html>`_.
It enables researchers to easily create and send surveys within a single, seamless interface.
Please read the above entry on the details and functionalities of this survey tool.

We do understand that not every use case will require a survey.
It is for this reason that the inclusion of user surveys is an optional component.
Researchers can skip this step because there is no requirement for getting user feedback.

In addition to prompting in-app surveys, researchers have the option to add a custom rating below items.
The screenshot below shows an overview of how to add these rating questions.
Each question can be responded to with a thumbs-up or thumbs-down.

.. image:: img/tutorial_screenshots/tutorial_3.jpg
   :width: 700
   :alt: Surveys screen

Additionally, rating surveys/feedback can be defined as well (displayed above).
``Feedback Surveys``provides you with the option to formulate statements about a news article, which every participant will see in the mobile application, positioned immediately after the news article.
The participants can agree to (like) or disagree with (dislike) a statement.
The statements are the same for all the participants in an experiment.

.. _scrapers:

Scraper Pipeline
----------------

To create recommendations for users, you first need to have items to recommend.
The item format is specified in the `Database Collections <https://informfully.readthedocs.io/en/latest/database.html>`_ (see 'newsArticles ', which serves as the item collection for the news aggregator use case in this online tutorial).

To populate this collection, we have provided a separate `Item Scraper <https://informfully.readthedocs.io/en/latest/scrapers.html>`_.
Please read the documentation on how to deploy it.
The source code is available for download in the `Scrapers Repository <https://github.com/Informfully/Scrapers>`_.

.. image:: img/tutorial_screenshots/tutorial_4.jpg
   :width: 700
   :alt: Items screen

We recommend running the scrapers on the same server as the other parts of the back end.
There is no communication happening between the scraping modules and any other component of Informfully.
You can set the scraper up so that it writes directly to MongoDB's document collection, ``newsArticles``/``itemCollection``.

.. _recommender:

Recommender System
------------------

By default, all items in  ``newsArticles``/``itemCollection`` will be shown in chronological order.
However, there is an option to connect an external recommender system framework to the Informfully back end, allowing for ranked user recommendations.

To have users receive personalized recommendations, the collection ``recommendationLists`` (see `Database Collections <https://informfully.readthedocs.io/en/latest/database.html>`_) needs to be populated.
Below this paragraph is a reference implementation of how to create recommendations for a single user.
(We advise using the official package for creating ``ObjectId``-records).

.. code-block:: python

    from bson.objectid import ObjectId

    # A single article recommendation for a user
    def create_recommendation(user, article_id, prediction, algorithm_id, preview):

        recommendation = {
            "_id": ObjectId(),
            "userId": user,
            "articleId": article_id,
            "prediction": prediction,
            "recommendationAlgorithm": algorithm_id,
            "isPreview": preview,
            "createdAt": datetime.now()
        }

        return recommendation

.. note::

    We provide an in-depth `recommendation list tutorial <https://informfully.readthedocs.io/en/latest/recommendations.html>`_ on how to connect your recommender framework with the Informfully back end and the `relevant code <https://github.com/Informfully/Documentation/tree/main/sample>`_.

The implementation of the recommendation list is framework-agnostic.
All that is needed is to write this data to ``recommendationLists`` in MongoDB.
Researchers can put this behind their own API, or they can run the recommender system on the same back end server as the other components of Informfully (thus directly writing to the database).

This step then concludes the setup of the user experiment.
Once you have completed this, the Informfully instance is ready to host and launch user experiments.

Once you have completed this setup, your Informfully instance is ready to host and launch user experiments.
Please look at the `Experiment Overview <https://informfully.readthedocs.io/en/latest/overview.html>`_ to see how these components interact with each other over the course of the different experimental phases.

.. _example:

Dataset Example
---------------

Visit the `Informfully Datasets Repository <https://github.com/Informfully/Datasets>`_ for getting access to the data, and please see the `relevant database documentation <https://informfully.readthedocs.io/en/latest/database.html>`_ for the technical documentation of all collections.
Below, you will find a quick overview of the dataset, which includes A) daily active users, B) daily interactions, C) topic overview, and D) word length distribution of news articles (referenced via URLs only).

.. image:: img/database_screenshots/statistics_plot.png
   :width: 700
   :alt: Informfully app screenshots
