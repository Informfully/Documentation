Data Augmentation
=================

For the code, please see the `augmentation filder <https://github.com/Informfully/Recommenders/tree/main/cornac/augmentation>`_ in the repository.

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides and overview of all components.
  And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.

Named Entity Recognition
------------------------------

The Named Entity Recognition (NER) feature identifies and counts named entities in the text.
The output requires post-processing to be used as a metric.
Supported languages are English to include Catalan, Chinese, Croatian, Danish, Dutch, Finnish, French, German, Greek, Italian, Japanese, Korean, Lithuanian, Macedonian, Norwegian, Polish, Portuguese, Romanian, Russian, Slovenian, Spanish, Swedish, Ukrainian, and multilingual datasets.
Given the item ID, item text, item language, and the type of entities, named entities can be extracted for the specified language.

Users can specify the type of entities to extract, such as person, event, or location (spaCy, a Python NLP library, will extract the named entities from the given text).
For English and Chinese datasets, entities can include: 'CARDINAL', 'DATE', 'EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 'NORP', 'ORDINAL', 'ORG', 'PERCENT', 'PERSON', 'PRODUCT', 'QUANTITY', 'TIME', and 'WORK_OF_ART'.
For other datasets, entities can include: 'LOC', 'MISC', 'ORG', and 'PER'.
Once entities are extracted, the function clusters similar named entities using the Louvain community detection algorithm and computes their frequency.
