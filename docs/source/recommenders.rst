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
It includes the four dedicated stages for pre-processing, in-processing, post-processing, and evaluation.
In addition to that, it features a save state manager where results of any stage can be stored and loaded.
This allows reusing existing data, e.g., for applying different re-rankers to one and the same candidate list.
Please find below an outline of the individual components and a link to their dedicated wiki pages for more information.

* `Data Augmentation <https://informfully.readthedocs.io/en/latest/augmentation.html>`_
* `Data Splitting <https://informfully.readthedocs.io/en/latest/splitting.html>`_ 
* `Model Selection - Participatory Diversity <https://informfully.readthedocs.io/en/latest/participatory.html>`_
* `Model Selection - Deliberative Diversity <https://informfully.readthedocs.io/en/latest/deliberative.html>`_
* `Model Selection - Random Walks <https://informfully.readthedocs.io/en/latest/randomwalk.html>`_
* `Model Selection - Neural Baselines <https://informfully.readthedocs.io/en/latest/neural.html>`_
* `Re-rankers Selection <https://informfully.readthedocs.io/en/latest/reranker.html>`_
* `Metrics Assessment <https://informfully.readthedocs.io/en/latest/metrics.html>`_
* `Item Visualization <https://informfully.readthedocs.io/en/latest/recommendations.html>`_
