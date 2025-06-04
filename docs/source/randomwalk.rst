Random Walks
============

Recommender systems are crucial in navigating the vast amount of content available on digital platforms.
Traditional methods often promote popular items, leading to a concentration in user exposure.
Random walk algorithm are designed to address this issue by promoting item diversity and accuracy in recommendations instead.

User Scoring
------------

With random walks, the user score functions as a representation of each user weight within the recommendation graph, influencing their impact on the recommendation results.
Given that we employ the random walk algorithm within the Cornac framework to produce randomized recommendations, we initialize the scores of all known users to 0 in this study.
This initialization ensures that, at the outset, each user is assigned an equal weight, effectively treating all users equally within the recommendation process and minimizing any bias in the initial state of the algorithm.

Graph Construction
------------------

The input data required by this algorithm includes the user reading history, a mapping table for user IDs and indices, and a mapping table for article IDs and indices.
The latter two are stored in the object after Radiosplit, making them easy to retrieve and use.
However, for the reading history, we need to construct it using the user-item rating matrix as a triple.
We load the triple data into a data frame and then use grouping and filtering functions to isolate the articles that each user has read (where rating=1), forming the reading history list.
By processing the entire DataFrame, we can extract the reading history for each user from the user-item interaction rating triple.

Algorithm Overview
-------------------

* RP3-β: Random walk that re-ranks items based on n-hop random walk transition probabilities, which can provide highly accurate and diverst recommendations. (`Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/rp3_beta>`_, `Paper <https://dl.acm.org/doi/abs/10.1145/2792838.2800180>`_)
* RWE-D: Random walk with Erasure (RWE-D) adds a popularity discount to items, for promoting the long-tail distribution. (`Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/rwe_d>`_, `Paper <https://dl.acm.org/doi/abs/10.1145/3442381.3449970>`_)
* D-RDW: Diversity-Driven Random Walks (D-RDW) aims to generate diverse recommendations that align with user-specified target distributions across multiple diversity dimensions. ( `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/drdw>`_)
