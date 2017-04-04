# -*- coding: utf-8 -*-

__author__ = """Michael E. Rose"""
__email__ = 'Michael.Ernst.Rose@gmail.com'
__all__ = ['euclidean', 'gindex', 'hindex']


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .metrics import *
