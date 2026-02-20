"""Tests for `metrics` module."""

import numpy as np

from scholarmetrics import euclidean, gindex, hindex


def test_euclidean():
    citations = [6, 10, 5, 46, np.nan, 2]
    received = euclidean(citations)
    expected = 47.75981574503821
    assert received == expected


def test_euclidean_with_nan():
    citations = [6, 10, 5, 46, np.nan, 2]
    received = euclidean(citations, ignore_nan=False)
    assert np.isnan(received)


def test_gindex():
    citations = [50, 7, 4, 18, 11, 3, np.nan]
    received = gindex(citations)
    expected = 6
    assert received == expected


def test_gindex_with_zeros():
    citations = [50, 7, 0, np.nan, 4, 18, 11, 0, 3]
    received = gindex(citations)
    expected = 6
    assert received == expected


def test_hindex():
    citations = [6, 10, 5, 46, 0, 2]
    received = hindex(citations)
    expected = 4
    assert received == expected


def test_hindex_with_nan():
    citations = [6, 10, 5, 46, np.nan, 2]
    received = hindex(citations)
    expected = 4
    assert received == expected


def test_hindex_with_only_nan():
    citations = [np.nan, np.nan]
    received = hindex(citations, ignore_nan=False)
    assert np.isnan(received)

