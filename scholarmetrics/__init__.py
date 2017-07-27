# -*- coding: utf-8 -*-

__author__ = """Michael E. Rose"""
__email__ = 'Michael.Ernst.Rose@gmail.com'
__all__ = ['euclidean', 'gindex', 'hindex']

from pbr.version import VersionInfo

_v = VersionInfo('scholarmetrics').semantic_version()
__version__ = _v.release_string()
version_info = _v.version_tuple()

from .metrics import *
