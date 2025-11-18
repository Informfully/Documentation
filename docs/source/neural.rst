Neural Models
=============

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides an overview of all components.
  And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.

Efficient Neural Matrix Factorization without Sampling (ENMF)
-------------------------------------------------------------

The ENMF model is a neural recommendation approach that combines the strengths of matrix factorization and neural networks, learning user and item representations from the entire training data without sampling.
In other words, it does not rely on sampling techniques to learn user and item representations.
To learn from the entire training data, the model employs three optimization methods: user-based, item-based, and alternating. 

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/enmf>`_
* `Paper <https://dl.acm.org/doi/abs/10.1145/3373807>`_

Long- and Short-Term User Representation (LSTUR)
------------------------------------------------

LSTUR is a neural news recommendation approach that can learn both long- and short-term user representations. 
The core of this model is a news encoder and a user encoder. 
The news encoder learns representations of news articles from their titles and topic categories, and uses an attention network to highlight important words for informative representation learning. 
The user encoder learns representations of users from the history of the news articles they browsed. 
It consists of two modules, i.e., a short-term user representation model (STUR) to capture users' temporal interests, and a long-term user representation model (LTUR) to capture users' consistent preferences.

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/lstur>`_
* `Paper <https://aclanthology.org/P19-1033>`_

Neural News Recommendation with Personalized Attention (NPA)
------------------------------------------------------------

The NPA model is a neural news recommendation approach that uses personalized attention to learn user and news representations.
It employs a CNN news encoder to learn hidden representations of news articles (from news article titles).
The user encoder learns user representations from their browsing histories, while capturing relationships among the news articles they have read.
Both word- and news-level attention mechanisms are utilized to improve the representation learning process.

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/npa>`_
* `Paper <https://dl.acm.org/doi/abs/10.1145/3292500.3330665>`_

Neural News Recommendation with Multi-Head Self-Attention (NRMS)
----------------------------------------------------------------

The NRMS model is a neural news recommendation approach that uses multi-head self-attention to learn representations of news and users. 
The news encoder learns news representations from news article titles by modelling word interactions. 
The user encoder learns user representations based on their browsing histories, while capturing relationships among the news articles they have read. 
In addition, the model incorporates an attention mechanism that focuses on identifying important words in news titles to learn more significant news articles and user representations.

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/nrms>`_
* `Paper <https://aclanthology.org/D19-1671>`_

Variational Autoencoders for Collaborative Filtering (DAE)
----------------------------------------------------------

The DAE algorithm extends variational autoencoders to collaborative filtering for implicit feedback by applying a non-linear probabilistic model. 
This generative model employs a multinomial likelihood to model users' interaction histories and utilizes Bayesian inference for parameter estimation.
DAE reconstructs clean inputs from deliberately corrupted versions.
By learning to remove or model the noise in the input data, DAE can learn more robust representations.

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/dae>`_
* `Paper <https://dl.acm.org/doi/abs/10.1145/3178876.3186150>`_
