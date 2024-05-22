Database Collections
====================

All content scraped from an external resource is categorized as either text or multimedia (images, audio, and video).
It is important to note that due to copyright restrictions, it was decided not to store multimedia files in the Informfully database (the system only saves the URL to the media object in question).
This had the advantage of reducing the load on the Informfully server as the media item is streamed from the original host.
The disadvantage is that if the source removes the file in question, then users in Informfully can no longer access the item.
If the item modelity is text, however, the system will create and store a copy after applying data augmentation/pre-processing steps (all of which are optional and can be individually enabled or disabled, see `Scrapers Pipeline <https://informfully.readthedocs.io/en/latest/scrapers.html>`_).
