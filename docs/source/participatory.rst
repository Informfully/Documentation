Participatory Diversity
=======================

``Political Diversity`` is an algorithm that creates recommendation list by using political user scores and political article scores.
This algorithm takes these user and article scores, computing the Euclidean distance to generate candidate items, and filters.

Overview
--------

There are three main issues that need to be addresses.
1) How to determine the normative distribution of news articles.
2) How to quantify and discretize this distribution into a 1D list or 2D grid.
3) How to translate the distribution into a matrix for a recommendation.

The model can calculate recommendations on a group level, reducing the overall runtime as it generates candidate lists.
This is possible because the political user score is the only attribute that is considered.
And this attribute can be defined in such a way that users are in pre-defined bins.
Hence, users in the same bin share the same score and should therefore receive the same recommendations.
It is up to researchers to define the distribution (e.g., users can only receive items from nearby bins in close proximity or on the opposite side of the spectrum).

PLD is supposed to be primarily used in an online setting.
In a first step, (baseline) users take a survey and are assigned a political score and read article.
In a second step, each article gets assigned the average political score of its readership.
(Both user scores and article scores are mapped into the same political space.)
Finally, users in the experimental group get recommended items based on user-item distance.

When re-usingsing PLD for offline testing requires addressing one critical issue:
There are no users that can take a survey.
When starting the offline evaluation, users are assigned political scores on the basis of the ration of political actors items in their history.
To that end, we introduce an offline-only step for annotating political actors/parties in news articles.
They are automatically counted across all reading histories.
The subsequent logic of PLD remains the same:
1) Baseline users read articles.
2) New articles get assigned a score on the basis of the average political score of its readership.
3) Users in the experimental group receive article recommendations based on the distance between their own political score and the score of the article.

Implementation
--------------

Input: ...

Output: ...

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
