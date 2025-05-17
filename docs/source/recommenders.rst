Recommender Pipeline
==================

This overview outlines the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository. 
It can be used in combination with the Informfully Research Platfrom or in a stand-alone fashion.
Informfully Recommenders is an extension of `Cornac <https://github.com/PreferredAI/cornac>`_.
And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.
Once you have developed your final pipeline, you can connect it to your database and rung it with, e.g., cron jobs.

* Pre-processing Stage: ...
* In-processing Stage: ...
* Post-processing Stage: ...
* Evaluation and Visualization Stage: ...
* Save state manager: Results of any stage can be stored and loaded; this allows re-using existing data, e.g., for applying different re-rankers to one and the same candidate list.

Cornac-internal representations are used for the item pool, candidate list, and recommendation lists across these stages.
Within stages, however, you can use raw IDs.
This allows you to reference external sources, as you can directly refer to them via IDs you already know (e.g., to combine with external resources).

1. Pre-processing Stage
-----------------------

Work in progress...

`Data loading <https://informfully.readthedocs.io/en/latest/loading.html>`_.

Work in progress...

`Data augmentation <https://informfully.readthedocs.io/en/latest/augmentation.html>`_.

2. In-processing Stage
----------------------

It support all existing algorithms and offers three new families of recommenders:
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

`Dynamic re-rankers <https://informfully.readthedocs.io/en/latest/dynamicreranker.html>`_.

4. Evaluation Stage
-------------------------------------

Work in progress...

`Metrics assessment <https://informfully.readthedocs.io/en/latest/metrics.html>`_.

Work in progress...

`Item visualization <https://informfully.readthedocs.io/en/latest/recommendations.html>`_.
