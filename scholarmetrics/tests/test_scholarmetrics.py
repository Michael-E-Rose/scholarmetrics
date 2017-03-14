#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `scholarmetrics` module."""


import unittest

from scholarmetrics.scholarmetrics import hindex


class TestScholarmetrics(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hindex(self):
        citations = [6, 10, 5, 46, 0, 2]
        received = hindex(citations)
        expected = 4
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
