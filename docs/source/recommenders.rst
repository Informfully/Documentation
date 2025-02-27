Recommender System
==================

This documentation provides an outline and tutorial on how to use `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_.
We recommend you start getting familiar with the underlying data first.
To do so, we prepared two overview pages.
Please see the `article and item ID overview page <https://informfully.readthedocs.io/en/latest/compass.html>`_ for details on how to access and retrieve the relevant user/item IDs used in this tutorial.
The IDs ted in the .

.. note::

  This tutorial outlines the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository. 
  It can be used in combination with the Informfully platfrom or in a stand-alone fashion.
  You can skip this introduction here for creating recommendations and go directly to the `item overview <https://informfully.readthedocs.io/en/latest/items.html>`_ to look at how entries must be stored.
  Afterwards, see the `relevant documentation <https://informfully.readthedocs.io/en/latest/recommendations.html>`_ on how to forward your item lists to the Informfully front end if you are using your own recommender system.

Pipeline Overview
-----------------

.. image:: img/recommender_assets/extended_pipeline.png
   :width: 700
   :alt: Informfully Recommenders Pipeline

* Pre-processing Stage
* In-processing Stage
* Post-processing Stage
* Evaluation Stage
* Savestate Manager

Work in progres...

Recommender Algorithms
----------------------

The ``Political Diversity`` algorithm is based on user scores and article scores.
The user score can be calculated from a questionnaire survey or based on the user's historical browsing data as adopted in this project, while the article score is calculated from the user scores of all its readers.
At the same time, the algorithm also requires a distribution to describe the number of articles that the system should recommend for a certain user score. 

The ``Exposure Diversity`` algorithm is based on the articles of the majority party and the minority party and the user's attributes.
It requires the user to pre-configure the party attributes and the user's political type (a random assignment strategy is adopted in this project, that is, randomly assigning a political type to the user).
The continuous exposure length of majority party articles and minority party articles, political articles and non-political articles is controlled by parameters to increase the diversity of recommendation results. 

For more information on the algorithms, please have a look at their dedicated pages:

* `Participatory Diversity <https://informfully.readthedocs.io/en/latest/participatory.html>`_
* `Deliberative Diversity <https://informfully.readthedocs.io/en/latest/deliberative.html>`_
* `Random Walk (with Popularity Discount) <https://informfully.readthedocs.io/en/latest/randomwalk.html>`_
* `Diversity Random Walk (for Political News) <https://informfully.readthedocs.io/en/latest/diversitywalk.html>`_

Item Re-ranker
--------------

`Item re-ranker <https://informfully.readthedocs.io/en/latest/reranker.html>`_.

Work in progress...

Savestate Manager
-----------------

`Savestate manager <https://informfully.readthedocs.io/en/latest/manager.html>`_.

Work in progress...

Recommendation Lists
--------------------

`Recommendation lists <https://informfully.readthedocs.io/en/latest/recommendations.html>`_.

Work in progress...

Tutorial Notebook
-----------------

`Tutorial notebook <https://informfully.readthedocs.io/en/latest/tutorial.html>`_.

Work in progress...
