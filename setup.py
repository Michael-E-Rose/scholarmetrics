#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import scholarmetrics
import versioneer

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
]

setup(
    name='scholarmetrics',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Compute scholarly metrics in Python with Pandas and NumPy",
    long_description=readme + '\n\n' + history,
    author="Michael E. Rose",
    author_email='Michael.Ernst.Rose@gmail.com',
    url='https://github.com/Michael-E-Rose/scholarmetrics',
    packages=[
        'scholarmetrics',
    ],
    package_dir={'scholarmetrics':
                 'scholarmetrics'},
    entry_points={
        'console_scripts': [
            'scholarmetrics=scholarmetrics.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='scholarmetrics',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    test_suite='nose.collector',
    tests_require=['nose']
)
