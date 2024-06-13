Informfully
===========

.. image:: img/logo_banner.png
   :width: 700
   :alt: Informfully banner logo

Welcome to the `Informfully <https://informfully.ch/>`_!
Informfully is a open-source reproducibility platform for content distribution and conducting user experiments.

This is the combined and official Informfully Documentation for all `code repositories <https://github.com/orgs/Informfully/repositories>`_.
For a tutorial on how to use Informfully, start with the :doc:`install` section and the :ref:`installation` instructions of the project.

**Links and Resources:** `Website <https://informfully.ch/>`_ | `Documentation <https://informfully.readthedocs.io/>`_ | `Informfully <https://github.com/orgs/Informfully/repositories>`_ | `DDIS@UZH <https://www.ifi.uzh.ch/en/ddis.html>`_

Overview
--------

This documentation provides you with all the information on successfully configure and deploy Informfully. It is structured as follows:

* **Getting Started** serves as an overall introduction to install the codebase, create a development environment, and notes on the deployment.
* **Running Experiments** provide a in-depth overview of how to use the Informfully platform to conduct user studies.
* **Technical Documentation** provide the same insights for various technical aspects in order to customize and extend the platform.
* **User Guides** prides tips and tricks into working with the codebase and provides useful links to tutorials (as this documenation is not a tutorial on how to use React Native and Meteor).

.. note::

    There are two different ways of how you can use Informfully: 
    1) use the front end and back end deployed by the University of Zurich or 
    2) deploy the whole application on your own.
    The upcoming tutorial focuses on the self-hosted deployment of Informfully.
    If you want to use the Informfully Platform as a cloud service, hosted at the University of Zurich, please reach out to us: info@informfully.ch

.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   install
   development
   deployment
   native

.. toctree::
   :maxdepth: 1
   :caption: Running Experiments

   overview
   experiment
   users
   surveys
   scrapers
   app

.. toctree::
   :maxdepth: 1
   :caption: Technical Documentation

   server
   database
   publications
   methods

.. toctree::
   :maxdepth: 1
   :caption: User Guides

   source
   docker
   google
   apple

Citation
--------

If you use any Informfully code/repository in a scientific publication, we ask you to cite the following papers:

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

Your are welcome to contribute to the Informfully ecosystem and become a part of your cummunity. Feel free to:

* fork any of the `Informfully repositories <https://github.com/Informfully/Documentation>`_ and
* make changes and create pull requests.

Please post your feature requests and bug reports in our `GitHub issues <https://github.com/Informfully/Documentation/issues>`_ section.

License
-------

Released under the `MIT License <https://github.com/Informfully/Documentation/blob/main/LICENSE>`_. (Please note that the respective copyright licenses of third-party libraries and dependencies apply.)

.. image:: img/app_screens.png
   :width: 700
   :alt: Informfully app screenshots
