Diversity Metrics
=================

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides an overview of all components.
  And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.

Gini Coefficient
----------------

The Gini coefficient is calculated for three different features: category, sentiment, and party.
It quantifies the inequality across these three dimensions within a given recommendation list.
The smaller the value indicated, the higher the equality.
A value of 0 means perfect equality, a value of 1 means perfect inequality.
(In this context, diversity is equated to equality.)

* `Implementation <https://github.com/Informfully/Recommenders/blob/main/cornac/metrics/diversity.py>`_
* `Paper <https://api.semanticscholar.org/CorpusID:11075976>`_

(Expected) Intra-List Distance
--------------------

The intra-list distance is somputer for four different features: category, title (embeddings), sentiment, and party.
It calculates the average pairwise dissimilarity between items in the recommendation list.
The smaller the value indicated, the higher the similarity.
A value of 0 means perfect similarity, a value of 1 means perfect dissimilarity.
(In this context, diversity is equated to dissimilarity.)
Expected intra-list distance is a rank-warare version of intra-list distance, the same principles and interpretation applies.
The main difference is that it considers the position an relevance of an item for assigning a value.

* `Implementation <https://github.com/Informfully/Recommenders/blob/main/cornac/metrics/diversity.py>`_
* `Paper <https://api.semanticscholar.org/CorpusID:11075976>`_

RADio Divergence
----------------

* `Implementation <https://github.com/Informfully/Recommenders/blob/main/cornac/metrics/diversity.py>`_
* `Paper <https://dl.acm.org/doi/abs/10.1145/3523227.3546780>`_

.. list-table::
   :widths: 25 25 25 25 75
   :header-rows: 1

   * - Metric
     - Item Feature
     - Value Range
     - Details
     - Interpretation
   * - Activation
     - Sentiment
     - [0,1]
     - Compares the sentiment distribution between the recommendation list and the article pool.
     - A higher value indicates greater divergence in sentiment distribution between the recommendation list and the item pool.
   * - Calibration Category
     - Category
     - [0,1]
     - Compares the complexity distribution of the recommendation list with the user's category preferences (bases on their reading history).
     - A higher value indicates greater deviation from the user's category preferences.
   * - Calibration Category
     - Complexity
     - [0,1]
     - Compares the complexity distribution of the recommendation list with the user's complexity preferences (bases on their reading history).
     - A higher value indicates greater deviation from the user's complexity preferences.
   * - Fragmentation
     - Story
     - [0,1]
     - Quantifies the differences between story chain distributions in recommendation lists across users.
     - A higher value indicates greater variation in news story chains for the recommendation lists.
   * - Alternative Voices
     - Minority and majority ratio
     - [0,1]
     - Compares the proportion of minority and majority viewpoints between the recommendation list and the item pool.
     - A higher value indicated greater disparity between minority and majority representation in the recommendation list and item pool.
   * - Representation
     - Party mentions
     - [0,1]
     - Measures divergence in representation of political parties in the recommendation list and item pool.
     - A higher value indicates greater divergence between the party mentions in the recommended articles and the item pool.
     