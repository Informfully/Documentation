Deliberative Diversity
======================

``Exposure Diversity`` is a algorithm that implements a deliberative diversity model by providing news articles from a wide range of topics and viewpoints.
It emphasizes party visibility, particularly of minority parties, to enhance public awareness and to foster a more inclusive understanding of political discourse.
In each news recommendation list, articles with majority and minority views are displayed in the order of the interval set by the user.
For example, if the interval parameter is set to 3, when generating the recommendation list, the model will extract 3 articles with majority views, followed by 3 articles with minority views, and then repeat this operation until the recommendation list is filled.

Model
-----

Work in progress...

Example
-------

Work in progress...

Source
------

`Deliberative Diversity for News Recommendations - Operationalization and Experimental User Study <https://dl.acm.org/doi/10.1145/3604915.3608834>`_, Heitz *et al.*, Proceedings of the 17th ACM Conference on Recommender Systems, 813–819, 2023.

.. code-block:: console

   @inproceedings{heitz2023deliberative,
      title={Deliberative Diversity for News Recommendations: Operationalization and Experimental User Study},
      author={Heitz, Lucien and Lischka, Juliane A and Abdullah, Rana and Laugwitz, Laura and Meyer, Hendrik and Bernstein, Abraham},
      booktitle={Proceedings of the 17th ACM Conference on Recommender Systems},
      pages={813--819},
      year={2023}
   }
