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
In Informfully, the sentiment analysis is performed using a multilingual sentiment analysis model, namely `cardiffnlp/twitter-xlm-roberta-base-sentiment <https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment>`_, based on `XLM-RoBERTa <https://huggingface.co/docs/transformers/en/model_doc/xlm-roberta>`_ and pre-trained on eight languages (i.e., English, French, German, Arabic, Hindi, Italian, Portuguese, and Spanish).
The model is able to automatically detect the language of the input text and provide sentiment analysis accordingly.

Sentiment analysis is employed to calculate the activation metric, assessing the emotional tone or polarity expressed in a piece of text.

Input:
  * A string representing the text to be analyzed, such as a news article.

Output:
  * A value representing the sentiment score, which is a float between -1 and 1.

`Implementation available online. <https://github.com/Informfully/Recommenders/tree/main/cornac/augmentation/sentiment.py>`_

Named Entities
--------------

The Named Entity Recognition (NER) feature identifies and counts named entities in the text.
The output requires post-processing to be used as a metric.
The NER feature is implemented using the `spaCy <https://spacy.io/>`_ library, which supports the extraction of named entities from texts in various languages, such as English, Catalan, Chinese, Croatian, Danish, Dutch, Finnish, French, German, Greek, Italian, Japanese, Korean, Lithuanian, Macedonian, Norwegian, Polish, Portuguese, Romanian, Russian, Slovenian, Spanish, Swedish, Ukrainian, and multilingual datasets.
Users can specify the type of entities to extract, such as person, event, or location.
For English and Chinese datasets, entities can include: 'CARDINAL', 'DATE', 'EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 'NORP', 'ORDINAL', 'ORG', 'PERCENT', 'PERSON', 'PRODUCT', 'QUANTITY', 'TIME', and 'WORK_OF_ART'.
For other datasets, entities can include: 'LOC', 'MISC', 'ORG', and 'PER'.
Once entities are extracted, the function clusters similarly named entities using the Louvain community detection algorithm and computes their frequency.

Input:
  * A string representing the text to be analyzed, such as a news article and a list of entity types, such as ['PER', 'LOC', 'ORG', 'MISC'].

Output:
  * A list of dictionaries, each representing a named entity and its attributes, such as:
    * `text`: The text of the entity.
    * `alternative`: A list of alternative names or aliases for the entity.
    * `spans`: A list of tuples representing the start and end character indices of the entity in the input text.
    * `frequency`: The number of times the entity appears in the text.
    * `label`: The type of the entity (e.g., 'PER', 'LOC', 'ORG', etc.).

`Implementation available online. <https://github.com/Informfully/Recommenders/tree/main/cornac/augmentation/ner.py>`_

Once named entities are identified, they can be further enriched by querying `Wikidata <https://www.wikidata.org/wiki/Wikidata:Main_Page>`_ for additional information.
This additional pipeline can extend person entities with their given name, family name, occupation, political party, gender, citizenship, ethnicity, and place of birth, as well as political parties with their ideology. 
These enriched named entities can serve as a valuable resource for calculating various features, such as political viewpoints based on a person's party if they are a politician.

Input:
  * A list of dictionaries, each representing a named entity and its attributes.

Output:
  * A list of dictionaries with person and organization as key and their extended information as values.

`Implementation available online. <https://github.com/Informfully/Recommenders/tree/main/cornac/augmentation/enrich_ne.py>`_

Political Actors
----------------

The political actors feature identifies and quantifies the political affiliations and ideologies expressed in the text, whether through individuals or organizations.
More precisely, it detects political parties and candidates mentioned in the text and calculates their frequency.
This feature makes use of the named entity recognition feature and queries Wikidata to consolidate party aliases and abbreviations, thus, minimizing redundancy. 
These enhancements yield a more precise and concise output, providing a clearer representation of political party frequencies within the text.

The political actors/parties feature is used to calculate the representation metrics.

Input:
  * A list of dictionaries with named entities, the language of the text, and a dictionary with possible translations of parties. 

Output:
  * A dictionary with the party names as keys and their corresponding frequencies as values, such as {'Democratic Party': 5, 'Republican Party': 3}.

`Implementation available online. <https://github.com/Informfully/Recommenders/tree/main/cornac/augmentation/party.py>`_

Text Complexity or Readability
------------------------------

The readability feature assesses the complexity of a text. 
The complexity score is computed using the Python library `textstat <https://pypi.org/project/textstat/>`_ which implements the Flesch-Kincaid score. 
The library supports multiple languages including English (US and UK), Afrikaans, Bulgarian, Catalan, Croatian, Czech, Danish, Dutch, Estonian, French, Galician, German (Germany, Swiss, Austrian), Greek, Hungarian, Italian, Latvian, Lithuanian, Norwegian Bokmål, Norwegian Nynorsk, Polish, Portuguese (Portugal, Brazil), Romanian, Russian, Serbian (official, Latin), Slovak, Slovenian, Spanish, Swedish, Telugu, Ukrainian, and Zulu.
The parameters of the Flesch-Kincaid formula differ across languages and are adjusted based on linguistic research.
A lower score indicates a more complex text, while a higher score suggests greater readability.

The text complexity or readability feature is used to calculate the calibration metric.

Input:
  * A string representing the text to be analyzed, such as a news article.

Output:
  * A float representing the complexity score, such as 60.0.

`Implementation available online. <https://github.com/Informfully/Recommenders/tree/main/cornac/augmentation/readability.py>`_

Event Clusters
--------------

The event cluster feature groups news articles reporting on the same news event into clusters, rather than broadly categorizing them by topic, which is a typical limitation of conventional clustering approaches.
The method first transforms each article's text into a TF-IDF vector, capturing the unique relevance of words within the article.
Next, it calculates the cosine similarity between articles within a 3-day time window, where articles with similar content are more likely to be related to the same news event.
These pairwise similarities are represented as a graph, where each article is a node, and edges between nodes indicate textual similarity. 
The `Louvain heuristic algorithm <https://python-louvain.readthedocs.io/en/latest/>`_ is then applied to partition the graph into clusters. 
Each cluster represents a "story chain", grouping articles that report on the same event over time. 

Event or story clusters are used to assess fragmentation.

Input:
  * A list of news articles, each represented as a string of text. Each article should have a timestamp indicating when it was published and a category.

Output:
  * For each news article, a number indicating the cluster name.

`Implementation available online. <https://github.com/Informfully/Recommenders/tree/main/cornac/augmentation/story.py>`_

Category Assignment
-------------------

The category assignment feature determines the category or topic of an item, such as the subject matter of a news article.
The category of a text can be extracted using two methods:
* Using Metadata Information: If an external metadata file containing item IDs and corresponding categories is available, the system can merge the metadata with the dataset by linking the item IDs, similar to joining tables in a database.
  Input:
    * A string representing the text to be analyzed, such as a news article and a corresponding metadata file.
  Output:
    * A string or a list of strings representing the category, such as 'Finance' or ['Finance', 'Health'].

* Using Zero-Shot Classification: When metadata is unavailable, users can specify a list of potential category labels. A pre-trained zero-shot classifier, `bart-large-mnli <https://huggingface.co/facebook/bart-large-mnli>`_, stored locally and downloaded from `Hugging Face <https://huggingface.co>`_, can be used to analyze the item's text and assign the most suitable category.
  Input:
    * A string representing the text to be analyzed, such as a news article and a list of potential categories.
  Output:
    * A string representing the category, such as 'Finance', 'Health', or 'Sport'.

The category feature is used for calculating several diversity metrics, such as calibration, binomial diversity, the Gini coefficient, intra-list diversity, and expected intra-list diversity.

`Implementation available online. <https://github.com/Informfully/Recommenders/tree/main/cornac/augmentation/category.py>`_
