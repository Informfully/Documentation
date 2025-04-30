Recommender System
==================

This tutorial outlines the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository. 
It can be used in combination with the Informfully platfrom or in a stand-alone fashion.

.. note::

  If you want to use the built-in Informfully Recommenders, please visit this `tutorial page <https://informfully.readthedocs.io/en/latest/compass.html>`_ instead.

Pipeline Overview
-----------------

* Pre-processing Stage: ...
* In-processing Stage: ...
* Post-processing Stage: ...
* Evaluation and Visualization Stage: ...
* Save state manager: Results of any stage can be stored and loaded. This allows re-using existing data, e.g., for applying different re-rankers to one and the same candidate list.

Each stage is a self-contained unit.
Cornac-internal representations are used for the item pool, candidate list, and recommendation lists across these stages.
Within stages, however, you can use raw IDs.
This allows you to reference external sources, as you can directly refer to them via IDs you already know (e.g., to combine with external resources.).

1. Pre-processing Stage
-----------------------

Work in progress...

`Data loading <https://informfully.readthedocs.io/en/latest/data.html>`_.

Work in progress...

`Data augmentation <https://informfully.readthedocs.io/en/latest/augmentation.html>`_.

2. In-processing Stage
----------------------

Informfully Recommenders offers three families of recommenders:
1) normative recommenders,
2) random walks, and
3) neural models.

The ``Participatory Diversity`` algorithm is based on user scores and article scores.
The user score can be calculated from a questionnaire survey or based on the user's historical browsing data as adopted in this project, while the article score is calculated from the user scores of all its readers.
At the same time, the algorithm also requires a distribution to describe the number of articles that the system should recommend for a certain user score. 

`Participatory diversity <https://informfully.readthedocs.io/en/latest/participatory.html>`_

The ``Deliberative Diversity`` algorithm is based on the articles of the majority party and the minority party and the user's attributes.
It requires the user to pre-configure the party attributes and the user's political type (a random assignment strategy is adopted in this project, that is, randomly assigning a political type to the user).
The continuous exposure length of majority party articles and minority party articles, political articles and non-political articles is controlled by parameters to increase the diversity of recommendation results. 

`Deliberative diversity <https://informfully.readthedocs.io/en/latest/deliberative.html>`_

Work in progress...

`Random walks (RP3Beta and RWE-D) <https://informfully.readthedocs.io/en/latest/randomwalk.html>`_

Work in progress...

`Diversity-driven random walk (D-RDW) <https://informfully.readthedocs.io/en/latest/drdw.html>`_

Work in progress...

`Data splitting <https://informfully.readthedocs.io/en/latest/splitting.html>`_.

3. Post-processing Stage
------------------------

Work in progress...

`Static re-rankers <https://informfully.readthedocs.io/en/latest/reranker.html>`_.

Work in progress...

`Dynamic re-rankers <https://informfully.readthedocs.io/en/latest/dynreranker.html>`_.

4. Evaluation and Visualization Stage
-------------------------------------

Work in progress...

`Evaluation metrics <https://informfully.readthedocs.io/en/latest/metrics.html>`_.

Work in progress...

`Item visualization <https://informfully.readthedocs.io/en/latest/recommendations.html>`_.

5. Example Notebook
-------------------

Work in progress...

`Experiment (tutorial notebook) <https://informfully.readthedocs.io/en/latest/tutorial.html>`_.
