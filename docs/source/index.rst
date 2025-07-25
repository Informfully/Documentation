Informfully
===========

.. image:: img/logo_banner.png
   :width: 700
   :alt: Informfully banner logo

Welcome to `Informfully <https://informfully.ch/>`_!
Informfully is an open-source reproducibility platform for content distribution and conducting user experiments.

This is the combined and official Informfully Documentation for all `code repositories <https://github.com/orgs/Informfully/repositories>`_.
For a tutorial on how to use Informfully, start with the :doc:`install` section and the :ref:`installation` instructions of the project.

**Links and Resources:** `GitHub <https://github.com/orgs/Informfully>`_ | `Website <https://informfully.ch>`_ | `X <https://x.com/informfully>`_ | `DDIS@UZH <https://www.ifi.uzh.ch/en/ddis.html>`_ | `Google Play <https://play.google.com/store/apps/details?id=ch.uzh.ifi.news>`_ | `App Store <https://apps.apple.com/us/app/informfully/id1460234202>`_

.. note::

    There are two different ways that you can use Informfully: 
    1) Use the front end and back end deployed by the University of Zurich or 
    2) Deploy the whole application on your own.
    The upcoming tutorial focuses on the self-hosted deployment of Informfully.
    If you want to use the Informfully Platform as a cloud service, hosted at the University of Zurich, please reach out to us: info@informfully.ch

Overview
--------

The Informfully platform allows you to push algorithmically curated text, image, audio, and video content to users and automatically generates a detailed log of their consumption history.
It is a domain-agnostic and platform-independent solution to fit your specific needs.
The platform was designed to accommodate different experiment types through versatility, ease of use, and scalability.
It features three core components: 

* a front end for displaying and interacting with recommended items, 
* a back end for researchers to create and maintain user experiments, and 
* a simple JSON-based exchange format (JREX) for ranked item recommendations to interface with third-party services.

This documentation provides you with all the information you need to successfully configure and deploy Informfully. It is structured as follows:

* **Getting Started** serves as an overall introduction for installing the codebase, creating a development environment, and notes on the platform deployment.
* **Managing Experiments** provides an in-depth overview of how to use the Informfully platform to conduct user studies.
* **Recommender System** provides a tutorial on how to use the built-in Informfully recommender framework.
* **Technical Documentation** provides insights for various technical aspects in order to customize and extend the platform.

.. image:: img/informfully_assets/informfully_app_screens.png
   :width: 700
   :alt: Informfully app screenshots

.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   install
   development
   deployment
   native

.. toctree::
   :maxdepth: 1
   :caption: Managing Experiments

   overview
   experiment
   users
   surveys
   scrapers
   app
   compass
   items

.. toctree::
   :maxdepth: 1
   :caption: Recommender System
   
   recommenders
   augmentation
   splitting
   participatory
   deliberative
   randomwalk
   neural
   reranker
   metrics
   recommendations

.. toctree::
   :maxdepth: 1
   :caption: Technical Documentation

   server
   methods
   publications
   database
   source
   docker
   google
   apple

Citation
--------

If you use any Informfully code/repository in a scientific publication, we ask you to cite the following papers:

* `Informfully - Research Platform for Reproducible User Studies <https://dl.acm.org/doi/10.1145/3640457.3688066>`_, Heitz *et al.*, Proceedings of the 18th ACM Conference on Recommender Systems, 2024.

.. code-block:: console

   @inproceedings{heitz2024informfully,
      title={Informfully - Research Platform for Reproducible User Studies},
      author={Heitz, Lucien and Croci, Julian A and Sachdeva, Madhav and Bernstein, Abraham},
      booktitle={Proceedings of the 18th ACM Conference on Recommender Systems},
      pages={660--669},
      year={2024}
  }

* `Deliberative Diversity for News Recommendations - Operationalization and Experimental User Study <https://dl.acm.org/doi/10.1145/3604915.3608834>`_, Heitz *et al.*, Proceedings of the 17th ACM Conference on Recommender Systems, 813–819, 2023.

.. code-block:: console

   @inproceedings{heitz2023deliberative,
      title={Deliberative Diversity for News Recommendations: Operationalization and Experimental User Study},
      author={Heitz, Lucien and Lischka, Juliane A and Abdullah, Rana and Laugwitz, Laura and Meyer, Hendrik and Bernstein, Abraham},
      booktitle={Proceedings of the 17th ACM Conference on Recommender Systems},
      pages={813--819},
      year={2023}
   }

* `Benefits of Diverse News Recommendations for Democracy: A User Study <https://www.tandfonline.com/doi/full/10.1080/21670811.2021.2021804>`_, Heitz *et al.*, Digital Journalism, 10(10): 1710–1730, 2022.

.. code-block:: console

   @article{heitz2022benefits,
      title={Benefits of diverse news recommendations for democracy: A user study},
      author={Heitz, Lucien and Lischka, Juliane A and Birrer, Alena and Paudel, Bibek and Tolmeijer, Suzanne and Laugwitz, Laura and Bernstein, Abraham},
      journal={Digital Journalism},
      volume={10},
      number={10},
      pages={1710--1730},
      year={2022},
      publisher={Taylor \& Francis}
   }

Support
-------

You are welcome to contribute to the Informfully ecosystem and become a part of the community. Feel free to:

* fork any of the `Informfully repositories <https://github.com/Informfully/Documentation>`_ and
* make changes and create pull requests.

Please post your feature requests and bug reports in our `GitHub issues <https://github.com/Informfully/Documentation/issues>`_ section.

License
-------

Released under the `MIT License <https://github.com/Informfully/Documentation/blob/main/LICENSE>`_. (Please note that the respective copyright licenses of third-party libraries and dependencies apply.)

.. image:: img/app_screens.png
   :width: 700
   :alt: Informfully app screenshots
