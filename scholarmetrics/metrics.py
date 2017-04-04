#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Collection of common metrics for academic scholars."""
import numpy as np

__all__ = ['euclidean', 'gindex', 'hindex']


def euclidean(arr):
    """
    Calculate Euclidean index for an author.

    An Euclidean index of a vector is the square root of the sum of
    the squared elements.

    Parameters
    ----------
    arr : array-like
          Array of citations.

    Returns
    -------
    eui : int
         Euclidean index of the author for the given citations.

    Examples
    --------
    >>> from scholarmetrics import euclidean
    >>> citations = [6, 10, 5, 46, 0, 2]
    >>> euclidean(citations)
    47.75981574503821

    Notes
    -----
    The Euclidean index was originally proposed by
    Motty Perry and Philip J. Reny [eu]_.

    References
    ----------
    .. [eu] Perry, M. and P. J. Reny (2016):
           "How to Count Citations If You Must",
           *The American Economic Review*, 106(9), pp. 2722-2241.
           DOI: 10.1257/aer.20140850
    """
    eui = np.linalg.norm(arr)
    return eui


def gindex(arr):
    """
    Calculate g-index for an author.

    An g-index of x means that the author's top x publications
    together accumulated at least :math:`x^2` citations.

    Parameters
    ----------
    arr : array-like
          Array of citations.

    Returns
    -------
    gi : int
         g-index of the author for the given citations.

    Examples
    --------
    >>> from scholarmetrics import gindex
    >>> citations = [6, 10, 5, 46, 0, 2]
    >>> gindex(citations)
    6

    Notes
    -----
    The g-index was originally proposed by Leo Egghe [g]_.  It excludes
    uncited publications.

    References
    ----------
    .. [g] Egghe, L. (2006): "Theory and practise of the g-index",
           *Scientometrics*, 69(1), pp. 131–152.
           DOI: 10.1007/s11192-006-0144-7
    """
    arr = [n for n in arr if n > 0]
    cum_sr = np.cumsum(sorted(arr, reverse=True))
    sqr_idx = [n**2 for n in range(1, len(arr) + 1)]
    gi = sum([c >= i for (c, i) in zip(cum_sr, sqr_idx)])
    return gi


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
    The h-index was originally proposed by Jorge E. Hirsch [h]_.

    References
    ----------
    .. [h] Hirsch, J. E. (2005): "An index to quantify
           an individual's scientific research output",
           *National Academy of Sciences of the USA* 102(46).
           DOI:1 0.1073/pnas.0507655102
    """
    sr = sorted(arr, reverse=True)
    idx = range(1, len(sr) + 1)
    hi = sum([p <= c for (c, p) in zip(sr, idx)])
    return hi
