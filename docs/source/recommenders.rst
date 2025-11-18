Recommender System
====================

This overview outlines the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository. 
It can be used in combination with the Informfully Research Platform or in a stand-alone fashion.
Informfully Recommenders is an extension of `Cornac <https://github.com/PreferredAI/cornac>`_.
And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/recsys_2025>`_ for hands-on examples of everything outlined here.

.. image:: uml/framework_extension_v4.2.png
   :width: 700
   :alt: Overview of the extension stages

The diagram above shows the extended framework Informfully Recommenders provides.
It includes four dedicated stages: pre-processing, in-processing, post-processing, and evaluation.
Additionally, it features a save state manager that allows the results of any stage to be stored and loaded.
This allows for reusing existing data, e.g., applying different re-rankers to the same candidate list.
Please find below an outline of the individual components, along with a link to their dedicated wiki pages for further information.

Pre-processing Stage
--------------------

* `Data Loading <https://informfully.readthedocs.io/en/latest/loading.html>`_
* `Data Augmentation <https://informfully.readthedocs.io/en/latest/augmentation.html>`_

In-processing Stage
-------------------

* `Data Splitting <https://informfully.readthedocs.io/en/latest/splitting.html>`_ 
* `Participatory Diversity <https://informfully.readthedocs.io/en/latest/participatory.html>`_
* `Deliberative Diversity <https://informfully.readthedocs.io/en/latest/deliberative.html>`_
* `Random Walks <https://informfully.readthedocs.io/en/latest/randomwalks.html>`_
* `Neural Baselines <https://informfully.readthedocs.io/en/latest/neural.html>`_

Post-processing Stage
---------------------

* `Re-rankers <https://informfully.readthedocs.io/en/latest/reranker.html>`_
* `User Simulator <https://informfully.readthedocs.io/en/latest/simulator.html>`_

Evaluation Stage
----------------

* `Metrics <https://informfully.readthedocs.io/en/latest/metrics.html>`_
* `Visualization <https://informfully.readthedocs.io/en/latest/recommendations.html>`_
