Random Walks
============

This recommendation algorithm uses random walk sampling technology to ensure the accuracy of the recommendation while taking into account the diversity of the recommendation list.
The algorithms are all based on RP3's new graph vertex ranking algorithm.
It re-ranks items based on n-hop random walk transition probabilities, which can provide highly accurate recommendations while increasing the prominence of long-tail items at the top of the recommendation list.
Random walk with Erasure (RWE-D) adds a popularity discount to items, for promoting the long-tail distribution.
The Diversity-Driven Random Walk Model (D-RDW) aims to generate diverse recommendations that align with user-specified target distributions across multiple diversity dimensions.

RP3-β  
-----

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/rp3_beta>`_
* `Paper <https://dl.acm.org/doi/abs/10.1145/2792838.2800180>`_

RWE-D
-----

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/rwe_d>`_
* `Paper <https://dl.acm.org/doi/abs/10.1145/3442381.3449970>`_


D-RDW
-----

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/drdw>`_
* Paper (TBA)
