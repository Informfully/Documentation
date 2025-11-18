User Simulator
==============

This overview presents the user simulator and its dynamic re-rankers, which are included in Informfully Recommenders.
In this context, dynamic means that the re-rankers are applied multiple times per user session.
They take the candidate list from the model and re-rank the items based on intra-session user feedback.
To that end, the simulator allows for defining these intra-session browsing behaviors and patterns to simulate user interactions.

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides an overview of all components.
  And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.

User Simulator

Dynamic re-ranking requires an underlying user model that specifies how the item feed is being browsed.
We provide a sample template that can be customized and extended.
In the context of NRSs, the two default behaviors included in the framework are:
1) Users are more likely to click on articles from a category that they have previously read, and
2) Items higher up in the recommendation list are more likely to be clicked.

`Implementation <TBD>`_  

Dynamic Attribute Penalization (DAP)

DAP offers a dynamic intra-session re-ranking option that updates recommendations in response to user interaction.
It diversifies the recommendation list by penalizing items in upcoming sessions that share attributes with clicked ones.

`Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/rerankers/dynamic_attribute_penalization>`_
