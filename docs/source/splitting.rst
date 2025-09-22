Data Splitting
==============

Different data splitting techniques are offered to test how the distribution of certain characteristics across the training and test sets impacts the recommendation outcome.
The following list presents an overview of the available options that we have implemented in a separate `Splitting Script <https://github.com/Informfully/Recommenders/blob/main/cornac/eval_methods/stratified_split_diversity.py>`_

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides an overview of all components.
  And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.

Attribute-based Sorting
-----------------------

This method can be used to see if having more complex articles or articles with higher sentiment scores in the training set would lead the algorithm to recommend more complex or emotionally charged articles to users who prefer simpler content (thereby increasing the diversity of news that these users engage with).
For complexity and sentiment score, this method splits the dataset and only selects high-scoring items for the training set. 
(This option matches news IDs from user interactions with their corresponding sentiment scores, sorts these scores from highest to lowest, and then allocates a certain percentage of the articles with the highest sentiment scores to the test set; the remaining articles with higher scores are used for the training set.)

Diversity-based Subset Construction
-----------------------------------

This method can be used to investigate whether selecting more diverse data for training and testing can lead to more accurate and/or diverse recommendation results.
This can be used, e.g., to increase diversity levels specifically for users who already have a history of consuming more diverse news than the average.
The goal of this splitting approach is to see if training the algorithm on specific user segments increases or decreases the diversity across the final recommendation results.

Attribute-based Stratified Splitting
------------------------------------

Splitting by attributes allows for (re-) balancing the test and training set according to custom ratios.
It is offered for user rating, news category, text complexity, and article sentiment.

Diversity-based Stratified Splitting
------------------------------------

This method can be used to determine whether introducing diversity metrics into splitting the dataset will increase the diversity of news that users engage with.
The aim is to explore whether these diversity metrics can effectively broaden the range of content presented to users, enhancing their engagement by introducing them to varied types of news.

Clustering-based Stratified Splitting
-------------------------------------

By categorizing the data into clusters based on their similarities and principal components, we can create subsets that are representative of different segments within the data.
We then perform a stratified sampling within each cluster, ensuring that the training and test sets reflect the distribution of the clustered data.
This approach allows us to analyze the effects of clustering-based segmentation on model performance, enabling us to understand how well the model can generalize across different user segments or content groups identified by the clustering algorithms.
