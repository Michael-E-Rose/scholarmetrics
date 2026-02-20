from importlib.metadata import version

__version__ = version("scholarmetrics")

__author__ = """Michael E. Rose"""
__email__ = 'Michael.Ernst.Rose@gmail.com'
__all__ = ['euclidean', 'gindex', 'hindex']

from .metrics import *
