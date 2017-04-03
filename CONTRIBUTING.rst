.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/Michael-E-Rose/scholarmetrics/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

scholarmetrics could always use more documentation, whether as part of the
official scholarmetrics docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/Michael-E-Rose/scholarmetrics/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Respect the Respect the `Python Code of Conduct <https://www.python.org/psf/codeofconduct/>`_.

Get Started!
------------

Ready to contribute? Here's how to set up `scholarmetrics` for local development.

1. Fork the `scholarmetrics` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/scholarmetrics.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv scholarmetrics
    $ cd scholarmetrics/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.
   Feel free to add your name to `AUTHORS.rst <AUTHORS.rst>`_.

5. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

6. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. Adhere to `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_.
3. The pull request should work for Python 2.7, 3.3, 3.4 and 3.5, and for PyPy. Check
   https://travis-ci.org/Michael-E-Rose/scholarmetrics/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::


    $ python -m unittest tests.test_scholarmetrics
