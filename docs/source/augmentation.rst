Data Augmentation
=================

Work in progres...

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
