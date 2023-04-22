import sys

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version

__version__ = version("scholarmetrics")

__author__ = """Michael E. Rose"""
__email__ = 'Michael.Ernst.Rose@gmail.com'
__all__ = ['euclidean', 'gindex', 'hindex']

from .metrics import *
