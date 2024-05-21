Scraper Pipeline
================

Architecture Overview
---------------------

.. image:: img/content_scraper.png
   :width: 700
   :alt: Overview of the scraper architecture

File Structure
--------------

...

Scraper Collection
------------------

...

Article Collection
------------------

There are set default values for each field. By doing this, indexing can be used, improving the performance of queries.
If we used non-existing fields to signify the absence of an attribute, we would have to use the "$exists" keyword to distinguish between articles that have a certain attribute.
However, the $exists operator cannot use any index.

Pipeline Overview
-----------------

In addition to scraping websites, the pipeline includes duplicate detection.
Sometimes it can happen that news outlets change a small portion of the article text and publish it again.
Those duplicates are not desirable in our application, so we aim to detect and purge those duplicates.

The detection is done by splitting the text of an article into single sentences, and then compare those sentences to every article that has been published in the last few days.
If a large part of two articles is identical, the new article won't be added into the database as a new article.

Database Manager
----------------

...

Logging Module
--------------

...
