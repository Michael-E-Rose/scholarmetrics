#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `metrics` module."""


import unittest
import numpy as np

from scholarmetrics import euclidean, gindex, hindex


class TestMetrics(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_euclidean(self):
        citations = [6, 10, 5, 46, np.nan, 2]
        received = euclidean(citations)
        expected = 47.75981574503821
        self.assertEqual(received, expected)

    def test_euclidean_with_nan(self):
        citations = [6, 10, 5, 46, np.nan, 2]
        received = euclidean(citations, ignore_nan=False)
        self.assertTrue(np.isnan(received))

    def test_gindex(self):
        citations = [50, 7, 4, 18, 11, 3, np.nan]
        received = gindex(citations)
        expected = 6
        self.assertEqual(received, expected)

    def test_gindex_with_zeros(self):
        citations = [50, 7, 0, np.nan, 4, 18, 11, 0, 3]
        received = gindex(citations)
        expected = 6
        self.assertEqual(received, expected)

    def test_hindex(self):
        citations = [6, 10, 5, 46, 0, 2]
        received = hindex(citations)
        expected = 4
        self.assertEqual(received, expected)

    def test_hindex_with_nan(self):
        citations = [6, 10, 5, 46, np.nan, 2]
        received = hindex(citations)
        expected = 4
        self.assertEqual(received, expected)

    def test_hindex_with_only_nan(self):
        citations = [np.nan, np.nan]
        received = hindex(citations, ignore_nan=False)
        self.assertTrue(np.isnan(received))


if __name__ == '__main__':
    unittest.main()
