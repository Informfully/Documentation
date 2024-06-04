Scraper Pipeline
================

Nowadays, RSS feeds are ubiquitous on any news website.
These feeds include a list of news articles formatted as XML file.
The scrapers listed here access these lists and parses them with `Feedparser <https://github.com/kurtmckee/feedparser>`_.
For the purpose of, e.g., news recommendations, the extracted information from these inclue attributes such as URL, title, image, and lead.
The remainder of this page outlines how the sample scrapers work and interface with the remainder of the back end.

.. note::

   The scripts for the content scrapers can run on the same or a different server than the remainder of the Informfully back end.
   Running the scripts is not controlled by any element of the back end.
   There is no dedicated deployment step involved.
   Instead, the scrapers need to be part of a `cron job` running on the server.
   Communication with the other components of the back end is limited to writing items to the pre-defined document collection.

Architecture Overview
---------------------

Informfully is complemented by a dedicated content scraper.
The entire content scraper pipeline is written in Python and uses MongoDB for persistent storage of news items.
All you need to do is to run add a scraper to `the scraper package <https://github.com/Informfully/Scrapers/tree/main/scraperpackage/scrapers>`_ and call it in ``main.py``.
You find sample implementations in this folder as well.

The individual scraper modules (called ``scrape.py`` or ``scrape\_n.py``) are required to implement a scraping function ``scrape()``.
There are two main parts to the scraper.
The first part contains the scraper implementations that allow collecting/scraping online resources.
The second part is the processing pipeline for text normalization, cleaning, and subsequent steps before storing them in the database.

.. image:: img/content_scraper.png
   :width: 700
   :alt: Overview of the scraper architecture

Despite the goal of the scrapers being the same for all outlets, the different formats, types of sources of information, and paywalls on news outlets rendered the task of having only one scraper very challenging
Hence, the decision was made to have split scrapers, where one part consists of shared core functionalities of parsing HTML, and a second part of adjusting to particular news outlets.
Specifically, the scrapers for each outlet consist of two parts.
First, they get a list of the most recent articles with either URLs or an identifier for the API.
Second, they iterate through the list and obtain the necessary information by scraping the HTML page or directly accessing the API if possible.

File Structure
--------------

By splitting the scraping task into independent modules, this allows for source-specific scrapers.
The main program ``main.py`` will import all scraper modules and calls their ``scrape()`` function, expecting them to return a list of items.
Functionalities shared among the scrapers are stored in a separate utility file (``utils.py``, e.g., a function to create an item object ensures uniformity in object field naming and default values).
Before storing the items to the document collections, the scraper performs a series of cleaning steps (e.g., duplication detection and text normalization).

The codebase includes a dedicated database manager.
This module simplifies to establish a connection the the MongoDB database.
It retrieves the credentials as well as the SSH connection details from the ``.env`` file.
To use the MongoManager, first import it with ``From mongomanager import MongoManager``.

Then use the with keyword to open the connection. MongoManager will return a MongoClient object.
If the configuration uses SSH, it will automatically close the connection once outside the with block.
If it configured without SSH, the manager will simply create a ``MongoClient`` object with the given address.

.. code-block:: python

   with MongoManager() as db:
      articles = db.articles.find({}).fetch()

Article Collection
------------------

All content scraped from an external resource is categorized as either text or multimedia (images, audio, and video).
It is important to note that due to copyright restrictions, it was decided not to store multimedia files in the Informfully database (the system only saves the URL to the media object in question).
This had the advantage of reducing the load on the Informfully server as the media item is streamed from the original host.
The disadvantage is that if the source removes the file in question, then users in Informfully can no longer access the item.
If the item modelity is text, however, the system will create and store a copy after applying data augmentation/pre-processing steps.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Attributes
     - Type
     - Description
   * - ``_id``
     - String
     - ID of article
   * - ``articleType``
     - String
     - Can be one of three: text, video, or podcast. Indicates whether the article contains a video, an audio, or only text.
   * - ``title``
     - String
     - Title of the article.
   * - ``lead``
     - String
     - Lead of the article.
   * - ``body``
     - Array of Objects
     - Contains the article text as paragraphs. The paragraphs are objects of the array and they have two properties: type (String) and text.
   * - ``url``
     - String
     - URL through which the article can be accessed.
   * - ``image``
     - String
     - Optional field, the URL to the cover image of the article.
   * - ``multimediaURL``
     - String
     - Contains a link to a video or audio file. The field should be set to null if empty. Should be consistent with the field ``articleType`` (meaning that if we have a text articleType, multimediaURL is set to null).
   * - ``multimediaDurationInMillis``
     - Integer
     - The length of the multimedia file (video or audio) in ms. Should be set to 1 if ``articleType`` is text.
   * - ``datePublished``
     - Date
     - Time at which the article was published on the news outlet's website.
   * - ``dateScraped``
     - Date
     - Time at which the article was scraped.
   * - ``dateUpdated``
     - Date
     - Outlets might update the article contents. Instead of creating a new article, the contents of the previous version are updated.
   * - ``dateDeleted``
     - Date
     - Optional field, we are sometimes asked by the outlets to remove articles. Instead of deleting them, we add a dateDeleted entry. Articles with this entry will not be shown.
   * - ``author``
     - String
     - Can also be a press agency or sponsored content. In case of multiple authors, separate them with a comma (,) symbol.
   * - ``outlet``
     - String
     - Current options include BLICK, NZZ, TAGI, SRF, WOZ, or WW.
   * - ``primaryCategory``
     - String
     - The categoriy of an item.
   * - ``subCategories``
     - Array of Strings
     - The sub-categories of an article. This information is not always provided.
   * - ``language``
     - String
     - Langauge code of the article (e.g., en-US, de-CH, etc.)

.. note::
   
   Be aware that Android devices can only handle websites secured by an SSL certificate (i.e. only https websites and no http websites). Therefore, data fields like ``url`` or ``multimediaURL`` should only contain https websites.

There are set default values for each field.
By doing this, indexing can be used, improving the performance of queries.
If we used non-existing fields to signify the absence of an attribute, we would have to use the ``$exists`` keyword to distinguish between articles that have a certain attribute.
However, the ``$exists`` operator cannot use any index.

Scraping Pipeline
-----------------

The scraper tool of the system runs the following augmentation steps.
First, it optionally white-labels the news (i.e., removes any information pertaining to the source of the news article).
Second, the current pipeline automatically assigns an image to a news item if none is provided (it does so based on the title and lead of the article).
Third, the scraper does text normalization (e.g., adjustment of date and currency formatting) across all featured online sources.
Finally, for German and English, it runs a sentiment analysis, if available, that will generate additional flags for each article (flagging it as either expressing a negative or positive sentiment).
The following paragraphs will explain each of these steps in more detail.

**HTML Parsing** The article content, i.e., the text itself, does not come with the feed.
The article text for each article is taken from an API.
When an API is unavailable, the content is scraped from the HTML page of the URL.
To obtain the HTML code from the URL, the built-in python package `urllib <https://docs.python.org/3/library/urllib.html>`_ is used.
To simplify the process of extracting the relevant information out of an HTML page, `Beautiful Soup <https://www.crummy.com/software/BeautifulSoup>`_ is used to help parse the HTML content into an organized data tree with built-in methods to navigate, search and modify.
When scraping, the system ensures that all the necessary fields are initialized with default values if the data cannot be obtained using the scraper.

**RSS Scraper** RSS Scraper} Within the small selection of scrapers, a few do not precisely follow the pattern RSS feed.
We provided sample implementation for cases where the page's actual content is not directly included in the initial HTML data, i.e., whenever the content is dynamically loaded later on using JavaScript.
To automate this process, `Selenium <https:// www.selenium.dev>`_ along with `Geckodriver <https:// github.com/mozilla/geckodriver>`_ is used to open a browser, navigate to the URL and execute the JavaScript to get a finalized page, from which the article list can be extracted using Beautiful Soup.
The scraping of individual articles follows the same procedure as other HTML-based scrapers. 
Naturally, this kind of scraping feeds takes more time than RSS feeds since more processing is required to render a dynamic website.
After all articles have been scraped and are in a single list, the scraper will apply content preprocessing steps before writing them to the database.
The preprocessing steps are necessary to ensure that the articles are prepared to a state optimized for Informfully.
The mandatory preprocessing for articles currently consists of duplicate detection and text normalization.

**Duplication Detection** News outlets often take pre-written news articles from news agencies and publish them on their own websites.
When multiple news outlets take the same article, both instances will be scraped and put into the database.
Both articles will be shown in the app and because the name of the news outlet source is omitted, the user would see two virtually identical articles.
This is likely to be very confusing for the participant, so an additional step had to be present in the pipeline to detect and handle duplicate articles.
However, news outlets usually make some minor changes to the original article content to fit their own format.
Therefore, a plain equality check on the entire article text will not work.
In our implementation, the two articles are first split into n-grams, sequences of words from the the article text of a specific length.
Afterwards, a percentage is calculated of how many sentences are shared between the two articles. If the percentage is over a certain threshold, the two articles will be considered as duplicates.
Every new article from the scrapers will undergo this step. The articles are compared against each other and also from the existing articles in the database pairwise.
Due to the time relevancy of news articles, duplicates typically do not have a large time span between them, so the selection of articles from the database are limited by a time window of a few days.

**Text Normalization** Especially when directly scraped from the websites, news articles may contain idiosyncrasies such as spelling variants of words, formatting (numbers, dates, and headlines) as well as self-references (names of the publication).
These anomalies may indicate the source of the article, which is undesirable.
The goal of the normalization step is to remove them to ensure a uniform presentation for the app.
The normalization process is implemented as a list of tuples.
The first element in the tuple is a regular expression to detect the abnormalities, with the second element being the string of text that serves as the replacement.

Logging Module
--------------

A logging module has been created to log any meaningful event happening during the scraping.
Every single log will contain a short message, the location where it was logged, a timestamp and an id which uniquely identifies a single execution run of the scrapers.
This logging tool is particularly useful for troubleshooting errors.
Any abnormalities in the scraper pipeline should be handled in a timely manner.
Especially during an ongoing experiment, it is vital that the flow of new articles is not halted.
In the event of a fatal error in the pipeline, the administrator is notified immediately via email with all relevant information.
With the run id, other logs belonging to the same run can be queried from the database to get a timeline of events leading up to the error.
