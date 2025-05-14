Data Splitting
==============

Work in progres...

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides and overview of all components.
  And you can look at the `Tutorial Notebook <https://informfully.readthedocs.io/en/latest/tutorial.html>`_ for hands-on examples of everything outlined here.

Attribute-based Sorting
-----------------------

Work in progres...

Diversity-based Subset Construction
-----------------------------------

Work in progres...

Attribute-based Stratified Splitting
------------------------------------

Work in progres...

Diversity-based Stratified Splitting
------------------------------------

This method can be used to determining whether introducing diversity metrics into splitting the dataset will increase the diversity of news that users engage with.
The aim is to explore if these diversity metrics can effectively broaden the range of content presented to users, enhancing their engagement by introducing them to varied types of news.

Clustering-based Stratified Splitting
-------------------------------------

By categorizing the data into clusters based on their similarities and principal components, we can create subsets that are representative of different segments within the data.
We then perform a stratified sampling within each cluster, ensuring that the training and test sets reflect the distribution of the clustered data.
This approach allows us to analyze the effects of clustering-based segmentation on model performance, enabling us to understand how well the model can generalize across different user segments or content groups identified by the clustering algorithms.
