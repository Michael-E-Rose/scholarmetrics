===============================
scholarmetrics
===============================

Compute scholarly metrics in Python with Pandas and NumPy.


**Documentation**: https://scholarmetrics.readthedocs.io.

.. image:: https://img.shields.io/pypi/v/scholarmetrics.svg
        :target: https://pypi.python.org/pypi/scholarmetrics

.. image:: https://readthedocs.org/projects/scholarmetrics/badge/?version=latest
        :target: https://scholarmetrics.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://codeclimate.com/github/Michael-E-Rose/scholarmetrics/badges/gpa.svg
        :target: https://codeclimate.com/github/Michael-E-Rose/scholarmetrics
        :alt: Code Climate

.. image:: https://travis-ci.org/Michael-E-Rose/scholarmetrics.svg?branch=master
        :target: https://travis-ci.org/Michael-E-Rose/scholarmetrics
        :alt: Build Status


Examples
--------

* J.E. Hirsch's h-index or Hirsch-index:

.. code:: python

    >>> from scholarmetrics import hindex
    >>> citations = [6, 10, 5, 46, 0, 2]
    >>> hindex(citations)
    4

* Euclidean index:

.. code:: python

    >>> from scholarmetrics import euclidean
    >>> citations = [6, 10, 5, 46, 0, 2]
    >>> euclidean(citations)
    47.75981574503821


Contributing
------------

.. image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
     :target: https://github.com/Michael-E-Rose/scholarmetrics/issues
     :alt: Contributions welcome

Please see `CONTRIBUTING.rst <CONTRIBUTING.rst>`_.

For a list of contributors see `AUTHORS.rst <AUTHORS.rst>`_.

License
-------
MIT License, see `LICENSE <LICENSE>`_.
