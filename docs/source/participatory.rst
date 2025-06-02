Participatory Diversity
=======================

The participatory ``Political Diversity`` (PLD) is an algorithm that creates a recommendation list by using political user scores and political article scores.
PLD leverages user and article scores derived from interaction data to curate news feeds that reflect a broad spectrum of political views, thus supporting a healthier democratic environment.

For the code, please see the `PLD implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/models/pld>`_ in the repository.

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides an overview of all components.
  And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.

Overview
--------

PLD is an algorithm that forms a recommendation list by using political user score and article score.
The user score can be calculated from a questionnaire survey or based on the user's historical browsing data, as adopted in this project, while the article score is calculated from the user scores of all its readers.
In order to assess these scores and apply PLD, the following three questions must be answered:
1. How to measure political scores of users?
2. How to assign a political label to a news item?
3. How many articles of what political positions should users receive? (I..e, quantify and discretize a normative target distribution across a 1D list or 2D grid.)

The Figure below shows how PLD combined normative target distributions across two 1D lists into a 2D grid for recommendations.

.. image:: img/algorithms_assets/pld.jpg
   :width: 700
   :alt: Normative distribution for recommendations with PLD

The model can calculate recommendations on a group level, reducing the overall runtime as it generates candidate lists.
This is possible because the political user score is the only attribute that is considered.
And this attribute can be defined in such a way that users are in pre-defined bins.
Hence, users in the same bin share the same score and should therefore receive the same recommendations.
It is up to researchers to define the distribution (e.g., users can only receive items from nearby bins in close proximity or on the opposite side of the spectrum).

PLD is supposed to be primarily used in an online setting.
In a first step, (baseline) users take a survey and are assigned a political score, and read an article.
In a second step, each article gets assigned the average political score of its readership.
(Both user scores and article scores are mapped into the same political space.)
Finally, users in the experimental group get recommended items based on user-item distance.

When re-using PLD for offline testing requires addressing one critical issue:
There are no users who can take a survey.
When starting the offline evaluation, users are assigned political scores on the basis of the ratio of political actors' items in their history.
To that end, we introduce an offline-only step for annotating political actors/parties in news articles.
They are automatically counted across all reading histories.
The subsequent logic of PLD remains the same:
1. Baseline users read articles.
2. New articles get assigned a score on the basis of the average political score of their readership.
3. Users in the experimental group receive article recommendations based on the distance between their own political score and the score of the article.

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
