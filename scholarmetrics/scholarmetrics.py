#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Collection of common metrics for academic scholars."""

__all__ = ['hindex']


def hindex(arr):
    """
    Calculate h-index for an author.

    An h-index of x means that the author has at least x publications
    that have been cited at least x times.

    Parameters
    ----------
    arr : array-like
          Array of citations.

    Returns
    -------
    hi : int
         H-index of the author for the given citations.

    Examples
    --------
    >>> from scholarmetrics import hindex
    >>> citations = [6, 10, 5, 46, 0, 2]
    >>> hindex(citations)
    4

    Notes
    -----
    The h-index was originally proposed by Jorge E. Hirsch [1]_.

    References
    ----------
    .. [1] J. E. Hirsch (2005): "An index to quantify
           an individual's scientific research output",
           *National Academy of Sciences of the USA* 102(46).
           DOI:1 0.1073/pnas.0507655102
    """
    sr = sorted(arr, reverse=True)
    idx = range(1, len(sr) + 1)
    hi = sum([p <= c for (c, p) in zip(sr, idx)])
    return hi
