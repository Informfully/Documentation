Random Walks
============

This recommendation algorithm uses random walk sampling technology to ensure the accuracy of the recommendation while taking into account the diversity of the recommendation list.
The algorithm is based on RP3's new graph vertex ranking algorithm.
It re-ranks items based on n-hop random walk transition probabilities, which can provide highly accurate recommendations while increasing the prominence of long-tail items at the top of the recommendation list.
This is why the algorithm can take into account recommendation diversity.

RP3Beta
-------

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/rp3_beta>`_
* `Paper <https://dl.acm.org/doi/abs/10.1145/2792838.2800180>`_

RWE-D
-----

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/rwe_d>`_
* `Paper <https://dl.acm.org/doi/abs/10.1145/3442381.3449970>`_
