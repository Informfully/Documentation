Re-rankers
==========

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides an overview of all components.
  And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.

Greedy Kullback-Leibler Divergence (G-KL)
----------------------------------------

* `Implementation <https://github.com/Informfully/Recommenders/blob/main/cornac/metrics/diversity.py>`_
* `Paper <https://dl.acm.org/doi/abs/10.1145/3240323.3240372>`_

Diversity by Proportionality (PM-2)
-----------------------------------

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/rerankers/pm2>`_
* `Paper <https://dl.acm.org/doi/abs/10.1145/2348283.2348296>`_

Maximal Marginal Relevance (MMR)
--------------------------------

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/rerankers/mmr>`_
* `Paper <https://dl.acm.org/doi/pdf/10.1145/290941.291025>`_

Dynamic Attribute Penalization (DAP)
-------------

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/rerankers/dynamic_attribute_penalization>`_
*  TBA
