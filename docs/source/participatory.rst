Participatory Diversity
=======================

``Political Diversity`` is an algorithm that creates recommendation list by using political user scores and political article scores.
This algorithm takes these user and article scores, computing the Euclidean distance to generate candidate items, and filters.

Model
-----

There are three main issues that need to be addresses.
1) How to determine the normative distribution of news articles.
2) How to quantify and discretize this distribution into a 1D list or 2D grid.
3) How to translate the distribution into a matrix for a recommendation.

The model can calculate recommendations on a group level, reducing the overall runtime as it generates candidate lists.
This is possible because the political user score is the only attribute that is considered.
And this attribute can be defined in such a way that users are in pre-defined bins.
Hence, users in the same bin share the same score and should therefore receive the same recommendations.

Example
-------

Work in progres...

Source
------

`Benefits of Diverse News Recommendations for Democracy: A User Study <https://www.tandfonline.com/doi/full/10.1080/21670811.2021.2021804>`_, Heitz *et al.*, Digital Journalism, 10(10): 1710–1730, 2022.

.. code-block:: console

   @article{heitz2022benefits,
      title={Benefits of diverse news recommendations for democracy: A user study},
      author={Heitz, Lucien and Lischka, Juliane A and Birrer, Alena and Paudel, Bibek and Tolmeijer, Suzanne and Laugwitz, Laura and Bernstein, Abraham},
      journal={Digital Journalism},
      volume={10},
      number={10},
      pages={1710--1730},
      year={2022},
      publisher={Taylor \& Francis}
