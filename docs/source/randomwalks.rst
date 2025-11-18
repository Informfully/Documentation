Random Walks
============

Recommender systems are crucial in navigating the vast amount of content available on digital platforms.
Traditional methods often promote popular items, leading to a concentration of user exposure.
Random walk algorithms are designed to address this issue by promoting item diversity and accuracy in recommendations instead.
The following three algorithms are available:

* RP3-β: Random walk that re-ranks items based on n-hop random walk transition probabilities, which can provide highly accurate and diverse recommendations. (`Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/rp3_beta>`_, `Paper <https://dl.acm.org/doi/abs/10.1145/2792838.2800180>`_)
* RWE-D: Random walk with Erasure (RWE-D) adds a popularity discount to items, for promoting the long-tail distribution. (`Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/rwe_d>`_, `Paper <https://dl.acm.org/doi/abs/10.1145/3442381.3449970>`_)
* D-RDW: Diversity-Driven Random Walks (D-RDW) aims to generate diverse recommendations that align with user-specified target distributions across multiple diversity dimensions. (`Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/drdw>`_)

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides an overview of all components.
  And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.

User Scoring
------------

With random walks, the user score functions as a representation of each user's weight within the recommendation graph, influencing their impact on the recommendation results.
Given that we employ the random walk algorithm within the Cornac framework to produce randomized recommendations, we initialize the scores of all known users to 0 in this study.
This initialization ensures that, at the outset, each user is assigned an equal weight, effectively treating all users equally within the recommendation process and minimizing any bias in the algorithm's initial state.

Graph Construction
------------------

The input data required by this algorithm includes the user reading history, a mapping table for user IDs and indices, and a mapping table for article IDs and indices.
The latter two are stored in the object after Radiosplit, making them easily retrievable and usable.
However, for the reading history, we need to construct it using the user-item rating matrix as a triple.
We load the triple data into a data frame and then use grouping and filtering functions to isolate the articles that each user has read (where rating = 1), forming the reading history list.
By processing the entire DataFrame, we can extract the reading history for each user from the user-item interaction rating triple.

Normative Target Distributions
------------------------------

User scoring and graph constructions are features shared among all three algorithms.
D-RDW, however, has an extra post-processing step for item re-ranking that allows it to fulfill certain normative target distributions.
A normative target distribution (NTD) is similar to a kernel function that defines a set of distributions across a set of target dimensions.
They are normative insofar as the example provided in the `Online Tutorial <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ specified an NTD across a political space.
This NTS should increase viewpoint and topic diversity to promote informed opinion formation when reading news.
As such, it operationalizes a societal value as part of a recommender regime.
