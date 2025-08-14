Re-ranker Selection
===================

This overview presents the static re-rankers included in Informfully Recommenders.
In this context, static means that the re-rankers are applied only once per user session.
They take the candidate list from the model and re-rank items based on predefined target metrics.

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides an overview of all components.
  And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.

Greedy Kullback-Leibler Divergence (G-KL)
-----------------------------------------

The Greedy-KL method re-ranks recommendations to closely match a user-defined target distribution, which can cover several dimensions.
More precisely, the G-KL re-ranker enhances the diversity of recommendation lists by minimizing the Kullback-Leibler (KL) divergence between the actual distribution of recommended items and a user-defined target distribution.
The Greedy-KL method allows end-users to define a custom target distribution and specify the diversity dimensions they are interested in (e.g., sentiment, category, political mentions, etc.). 
Users can also assign weights to these dimensions, prioritizing certain dimensions of diversity over others. 
This method incrementally builds a ranked list of recommendations by iteratively selecting items that best achieve the target distribution.

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/rerankers/greedy_kl>`_
* `Paper <https://dl.acm.org/doi/abs/10.1145/3240323.3240372>`_

Diversity by Proportionality (PM-2)
-----------------------------------

The PM-2 re-ranker promotes diversity in recommendation lists by ensuring that the selected items reflect a proportional representation of various aspects (e.g., diversity, relevance, etc.).  
The goal of the re-ranker is to generate an optimally ranked list such that the number of relevant items for each aspect is proportional to the overall popularity of that particular aspect. 
The items are selected iteratively, such that at each rank, the algorithm selects the item that maximizes the proportionality score, or the item that represents aspects that have been covered less at previous ranks.
This process continues until the desired length of the recommendation list is achieved.

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/rerankers/pm2>`_
* `Paper <https://dl.acm.org/doi/abs/10.1145/2348283.2348296>`_

Maximal Marginal Relevance (MMR)
--------------------------------

The Maximal Marginal Relevance (MMR) re-ranker balances relevance and diversity in recommendation lists by selecting items that are both relevant to the user and diverse from each other.
This is achieved through a tunable parameter λ, which linearly combines these two aspects into a single score, called marginal relevance. 
A document is considered to have high marginal relevance if it is relevant to the query and has minimal similarity to previously chosen documents. 
The MMR algorithm greedily selects the document with the highest marginal relevance score until it fulfills the desired length of the recommendation list.

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/rerankers/mmr>`_
* `Paper <https://dl.acm.org/doi/pdf/10.1145/290941.291025>`_

Dynamic Attribute Penalization (DAP)
------------------------------------

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/rerankers/dynamic_attribute_penalization>`_
*  Please see the `User Simulator <https://informfully.readthedocs.io/en/latest/simulator.html>`_ for the details on the dynamic re-ranking approach using DAP.
