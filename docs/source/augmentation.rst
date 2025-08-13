Data Augmentation
=================

For the code, please see the `augmentation folder <https://github.com/Informfully/Recommenders/tree/main/cornac/augmentation>`_ in the repository.

.. note::

  This tutorial outlines part of the workflow for the `Informfully Recommenders <https://github.com/Informfully/Recommenders>`_ repository.
  The `Recommenders Pipeline <https://informfully.readthedocs.io/en/latest/recommenders.html>`_ provides an overview of all components.
  And you can look at the `Tutorial Notebook <https://github.com/Informfully/Experiments/tree/main/experiments/tutorial>`_ for hands-on examples of everything outlined here.

Sentiment Analysis
------------------

The sentiment feature assesses the emotional tone or polarity expressed in a text. 
It generates a compound score that integrates individual scores for positivity, negativity, and neutrality, offering a comprehensive evaluation of the sentiment.
This compound score ranges from -1 (extremely negative) to 1 (extremely positive), reflecting the intensity of the sentiment expressed in the text.
In Informfully, the sentiment analysis is performed using a multilingual sentiment analysis model, namely `cardiffnlp/twitter-xlm-roberta-base-sentiment <https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment>`, based on `XLM-RoBERTa <https://huggingface.co/docs/transformers/en/model_doc/xlm-roberta>` and pre-trained on eight languages (i.e., English, French, German, Arabic, Hindi, Italian, Portuguese, and Spanish).
The model is able to automatically detect the language of the input text and provide sentiment analysis accordingly.

Sentiment analysis is employed to calculate the activation metric, assessing the emotional tone or polarity expressed in a piece of text.

Input:
* A string representing the text to be analyzed, such as a news article.

Output:
* A value representing the sentiment score, which is a float between -1 and 1.

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/augmentation/sentiment.py>`

Named Entities
--------------

The Named Entity Recognition (NER) feature identifies and counts named entities in the text.
The output requires post-processing to be used as a metric.
Supported languages are English to include Catalan, Chinese, Croatian, Danish, Dutch, Finnish, French, German, Greek, Italian, Japanese, Korean, Lithuanian, Macedonian, Norwegian, Polish, Portuguese, Romanian, Russian, Slovenian, Spanish, Swedish, Ukrainian, and multilingual datasets.
Given the item ID, item text, item language, and the type of entities, named entities can be extracted for the specified language.
Users can specify the type of entities to extract, such as person, event, or location (spaCy, a Python NLP library, will extract the named entities from the given text).
For English and Chinese datasets, entities can include: 'CARDINAL', 'DATE', 'EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 'NORP', 'ORDINAL', 'ORG', 'PERCENT', 'PERSON', 'PRODUCT', 'QUANTITY', 'TIME', and 'WORK_OF_ART'.
For other datasets, entities can include: 'LOC', 'MISC', 'ORG', and 'PER'.
Once entities are extracted, the function clusters similarly named entities using the Louvain community detection algorithm and computes their frequency.

Political Actors
----------------

The political actors/parties feature is used to calculate representation.
It identifies and quantifies the political affiliations and ideologies expressed in the text, whether through individuals or organizations.
By analyzing the frequency of political party mentions, this feature provides insights into the political stance of the content and is applied to representative metrics.


Text Complexity or Readability
---------------

The readability feature assesses the complexity of a text. 
The complexity score is computed using the Python library `textstat <https://pypi.org/project/textstat/>` which implements the Flesch-Kincaid score. 
The library supports multiple languages including English (US, UK), Afrikaans, Bulgarian, Catalan, Croatian, Czech, Danish, Dutch, Estonian, French, Galician, German (Germany, Swiss, Austrian), Greek, Hungarian, Italian, Latvian, Lithuanian, Norwegian Bokmål, Norwegian Nynorsk, Polish, Portuguese (Portugal, Brazil), Romanian, Russian, Serbian (official, Latin), Slovak, Slovenian, Spanish, Swedish, Telugu, Ukrainian, and Zulu.
The parameters of the Flesch-Kincaid formula differ across languages and are adjusted based on linguistic research.
A lower score indicates a more complex text, while a higher score suggests greater readability.

The text complexity or readability feature is used to calculate the calibration metric.

Input:
* A string representing the text to be analyzed, such as a news article.

Output:
* A float representing the complexity score, such as 60.0.

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/augmentation/readability.py>`

Event Clusters
--------------

Event or story clusters are a feature used to assess fragmentation.
The story chain method groups articles reporting on the same news event into clusters, rather than broadly categorizing them by topic, which is a typical limitation of conventional clustering approaches.
The method first transforms each article's text into a TF-IDF vector, capturing the unique relevance of words within the article.
Next, it calculates the cosine similarity between articles within a 3-day time window, where articles with similar content are more likely to be related to the same news event.

Category Assignment
-------------------

The category assignment feature determines the category or topic of an item, such as the subject matter of a news article.
The category of a text can be extracted using two methods:
* Using Metadata Information: If an external metadata file containing item IDs and corresponding categories is available, the system can merge the metadata with the dataset by linking the item IDs, similar to joining tables in a database.
  Input:
    * A string representing the text to be analyzed, such as a news article and a corresponding metadata file.
  Output:
    * A string or a list of strings representing the category, such as 'Finance' or ['Finance', 'Health'].

* Using Zero-Shot Classification: When metadata is unavailable, users can specify a list of potential category labels. A pre-trained zero-shot classifier, `bart-large-mnli <https://huggingface.co/facebook/bart-large-mnli>`, stored locally and downloaded from `Hugging Face <https://huggingface.co>`, can be used to analyze the item's text and assign the most suitable category.
  Input:
    * A string representing the text to be analyzed, such as a news article and a list of potential categories.
  Output:
    * A string representing the category, such as 'Finance', 'Health', or 'Sport'.

The category feature is used for calculating several diversity metrics, such as calibration, binomial diversity, the Gini coefficient, intra-list diversity, and expected intra-list diversity.

* `Implementation <https://github.com/Informfully/Recommenders/tree/main/cornac/augmentation/category.py>`
