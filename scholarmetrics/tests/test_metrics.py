#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `metrics` module."""


import unittest

from scholarmetrics import euclidean, gindex, hindex


class TestMetrics(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_euclidean(self):
        citations = [6, 10, 5, 46, 0, 2]
        received = euclidean(citations)
        expected = 47.75981574503821
        self.assertAlmostEqual(received, expected)

    def test_gindex(self):
        citations = [50, 7, 4, 18, 11, 3]
        received = gindex(citations)
        expected = 6
        self.assertEqual(received, expected)

    def test_gindex_with_zeros(self):
        citations = [50, 7, 0, 4, 18, 11, 0, 3]
        received = gindex(citations)
        expected = 6
        self.assertEqual(received, expected)

    def test_hindex(self):
        citations = [6, 10, 5, 46, 0, 2]
        received = hindex(citations)
        expected = 4
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
