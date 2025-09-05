Data Loading
============

This page provides an example for loading the MIND news dataset into the Cornac framework.
Users can similarly load their own datasets and create other loading functions. 
The functions detailed in the subsequent sections are available within the **``cornac/datasets/mind.py``** module.
The aim is to transform externally enhanced data into the requisite format required by the diversity framework.
Prior to employing functions, it is strongly advised to review the structure and content of the provided data file.
The following sections will provide an overview of all the functions offered.

load_feedback
-------------

This function is designed to handle rating data loading.
The necessary format involves a CSV file that includes three essential columns: user, item, and rating.
These columns must follow a specific order: user first, followed by item, and then rating.
However, if the CSV file contains an index and consequently has four columns, the ``load_feedback`` function will exclude the first column.
The output is a list of tuples containing all user-item-rating pairs.

load_sentiment
--------------

This function loads sentiment data associated with items.
The requisite data structure can take the form of a JSON file (recommended) or a CSV file.
For JSON files, the expected format is ``{item id: item sentiment_value}``.
For example::

    {
        "N55189": 0.6597,
        "N46039": -0.9932,
        "N51741": -0.4344
    }

In this structure, the keys represent the raw IDs of the items, while the corresponding values denote the sentiment values attributed to the articles.
Alternatively, if opting for a CSV file, the first column should contain the item IDs, and the second column should contain the corresponding sentiment values.
The output of this function is a dictionary containing items and their sentiment.

load_category
-------------

The purpose of this function is to load item categories into a dictionary.
This function pertains to scenarios where each item is linked to a single category.
The input can be provided in either a JSON format (recommended) or a CSV format.
When using a JSON file as input, the expected format is ``{item id: item category}``.
For example::

    {
        "N11276": "finance",
        "N264": "autos",
        "N40716": "tv",
        "N28088": "movies",
        "N43955": "entertainment"
    }

Alternatively, if opting for a CSV file as input, the first column should contain the item raw IDs, and the second column the corresponding category.
The output of this function is a dictionary containing item and item category information.

load_category_multi
-------------------

This function differs from **load_category** in two ways: it can accommodate either a single category or multiple categories per item.
The output is a dictionary mapping items to encoded category vectors.
Input can be JSON (recommended) or CSV.
For JSON input, the expected format is ``{item id: item categories}``.
For example::

    {
        "N55528": ["lifestyle", "health"], 
        "N18955": ["health", "sports"],
        "N61837": ["news", "weather"], 
        "N53526": "health",
        "N38324": ["health", "food"], 
        "N2073": "sports"
    }

For single-category items: ``{"N2073": "sports"}``  
For multi-category items: ``{"N55528": ["lifestyle", "health"]}``
For CSV input, the first column should list item raw IDs, and the second column should contain a single category or a comma-separated list.

load_complexity
---------------

This function loads item complexity values.
Supported formats: JSON (recommended) and CSV.
JSON expected format::

    {
        "N55189": 29.1167938931,
        "N46039": 14.9315415822,
        "N51741": 33.1415942029,
        "N53234": 12.4489795918
    }

The function will exclude items with NaN complexity values.
CSV: First column = item ID, second column = complexity (ensure valid numerical values).

load_story
----------

This function loads item story values into a dictionary.
Input formats: JSON (recommended) or CSV.
JSON expected format::

    {
        "N55189": 458.0,
        "N46039": 0.0,
        "N51741": 458.0,
        "N53234": 397.0
    }

CSV: First column = item ID, second column = story value (convertible to int).

load_entities
-------------

This function compiles party mentions per item.
JSON expected format::

    {
        "N38895": {
            "Democratic Party": 4
        },
        "N30924": {},
        "N58251": {
            "Republican Party": 2,
            "Federalist Party": 2,
            "Democratic Party": 2
        }
    }

CSV: First column = item ID, second column = comma-separated party names. Example:

+----------+----------------------------------------------------------------------------------------------+
| Item     | Entities                                                                                     |
+==========+==============================================================================================+
| N38895   | "Democratic Party,Democratic Party,Democratic Party,Democratic Party"                        |
| N58251   | "Republican Party,Republican Party,Federalist Party,Federalist Party,Democratic Party,..."   |
+----------+----------------------------------------------------------------------------------------------+

JSON input will filter out items with empty data. Output is a dictionary with lists of parties as values::

    {
        "N38895": ["Democratic Party", "Democratic Party", "Democratic Party", "Democratic Party"],
        "N58251": ["Republican Party", "Republican Party", "Federalist Party", "Federalist Party", "Democratic Party", "Democratic Party"]
    }

load_min_maj
------------

This function manages minority/majority scores based on a protected attribute like gender, ethnicity, or mainstream status.
The ``data_type`` parameter can be set to one of these.
Expected JSON format::

    {
        "N55189": {
            "gender": [0.0, 1.0],
            "ethnicity": [0.0, 1.0],
            "mainstream": [0.9412, 0.0588]
        },
        "N46039": {
            "gender": [0.0, 1.0],
            "ethnicity": [1.0, 0.0],
            "mainstream": [0.9333, 0.0667]
        }
    }

CSV format:  
- Column 1 = item ID  
- Column 2 = minority score  
- Column 3 = majority score  

Output: a dictionary mapping item IDs to numpy arrays: ``[minority, majority]``.

load_text
---------

This function retrieves text content for each item.

JSON expected format::

    {
        "N55189": "text",
        "N46039": "text"
    }

CSV: First column = item ID, second column = text.  
Returns: dictionary mapping IDs to text strings.

build
-----

This function transforms external item IDs into Cornac internal IDs. It requires:
- The data dictionary from loading functions, and
- ``id_map`` obtained after feeding user-item-rating data into Cornac.

Returns: dictionary mapping internal IDs to features. This is then used in initializing diversity metrics.
