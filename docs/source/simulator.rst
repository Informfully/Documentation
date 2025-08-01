User Simulator
==============

This overview present the user simulator and its dynamic re-rankers included in Informfully Recommenders.
In this context, danymic means that the re-rankers are applied multiple times per user session.
They take the candidate list from the model and re-rank the items based on intra-session user feedback.
To that end, the simulator allows to define these intra-session browsing behavior/patterns to mock user interactions.

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides an overview of all components.
  And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.

User Simulator

* `Implementation <TBD>`_
*  Dynamic re-ranking requires an underlying user model that specifies how the item feed is being browsed.
We provide a sample template that can be customized and extended.
In the context of NRSs, the two default behaviors included in the framework are:
1) Users are more likely to click on articles from a category that they have previously read, and
2) Items higher up in the recommendation list are more likely to be clicked.

Dynamic Attribute Penalization (DAP)

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/rerankers/dynamic_attribute_penalization>`_
*  Work in progress...
