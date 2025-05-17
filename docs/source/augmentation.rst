Data Augmentation
=================

For the code, please see the `augmentation filder <https://github.com/Informfully/Recommenders/tree/main/cornac/augmentation>`_ in the repository.

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides and overview of all components.
  And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.

Sentiment Analysis
------------------

The sentiment feature is employed to calculate the activation metric, assessing the emotional tone or polarity expressed in a piece of text.
Sentiment analysis typically generates a compound score that integrates individual scores for positivity, negativity, and neutrality, offering a comprehensive evaluation of the sentiment.
This compound score ranges from -1 (extremely negative) to 1 (extremely positive), reflecting the intensity of the sentiment expressed in the text.

Named Entities
--------------

The Named Entity Recognition (NER) feature identifies and counts named entities in the text.
The output requires post-processing to be used as a metric.
Supported languages are English to include Catalan, Chinese, Croatian, Danish, Dutch, Finnish, French, German, Greek, Italian, Japanese, Korean, Lithuanian, Macedonian, Norwegian, Polish, Portuguese, Romanian, Russian, Slovenian, Spanish, Swedish, Ukrainian, and multilingual datasets.
Given the item ID, item text, item language, and the type of entities, named entities can be extracted for the specified language.
Users can specify the type of entities to extract, such as person, event, or location (spaCy, a Python NLP library, will extract the named entities from the given text).
For English and Chinese datasets, entities can include: 'CARDINAL', 'DATE', 'EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 'NORP', 'ORDINAL', 'ORG', 'PERCENT', 'PERSON', 'PRODUCT', 'QUANTITY', 'TIME', and 'WORK_OF_ART'.
For other datasets, entities can include: 'LOC', 'MISC', 'ORG', and 'PER'.
Once entities are extracted, the function clusters similar named entities using the Louvain community detection algorithm and computes their frequency.

Political Actors
----------------

The political actors/parties feature is used to calculate representation.
It identifies and quantifies the political affiliations and ideologies expressed in the text, whether through individuals or organizations.
By analyzing the frequency of political party mentions, this feature provides insights into the political stance of the content and is applied to representative metrics.

Text Complexity
---------------

The text complexity or readability feature is used to calculate calibration by assessing the reading ease of text using the Flesch-Kincaid reading ease test.
A lower score indicates a more complex text, while a higher score suggests greater readability.
For example, the maximum possible readability score is 121.22 for an English text, while the score theoretically has no lower bound, allowing for negative values in cases of extreme complexity.

Event Clusters
--------------

Event or story clusters is a feature used to assess fragmentation.
The story chain method groups articles reporting on the same news event into clusters, rather than broadly categorizing them by topic, which is a typical limitation of conventional clustering approaches.
The method first transforms each article's text into a TF-IDF vector, capturing the unique relevance of words within the article.
Next, it calculates the cosine similarity between articles within a 3-day time window, where articles with similar content are more likely to be related to the same news event.

Category Assignment
-------------------

The category feature is a critical component for calculating several diversity metrics, such as calibration, binomial diversity, the Gini coefficient, intra-list diversity, and expected intra-list diversity.
This feature determines the category or topic of an item, such as the subject matter of a news article.
Users can extract the category feature using two methods:
