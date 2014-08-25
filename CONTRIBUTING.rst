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

Report bugs at https://github.com/codefortulsa/BPZAround.me/issues.

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

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

BPZAround.me could always use more documentation, whether as part of the
official BPZAround.me docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/codefortulsa/BPZAround.me/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

.. _get-started:

Get Started!
------------

Ready to contribute? Here's how to set up `BPZAround.me` for local development.

#. `Fork BPZAround.me`_ on GitHub.

#. `Clone`_ your fork locally::

    git clone git@github.com:your_name_here/BPZAround.me.git

#. Install requirements into a `virtualenv`_. This is easiest with
   `virtualenvwrapper`_::

    mkvirtualenv BPZAround.me
    cd BPZAround.me/
    pip install -r requirements.txt -r requirements.dev.txt

#. `Install PostGIS for GeoDjango`_.

#. Create a ``bpzaroundme`` PostGIS spatial database per the
   `Post-installation`_ instructions for your version of Postgres & PostGIS.::

#. Setup your local environment (Note: you can automate this with `autoenv`_)::

    source .env

#. Make sure tests work::

   $ ./manage.py test

#. Run it!::

   $ ./manage.py runserver

.. _`Fork BPZAround.me`: https://github.com/codefortulsa/BPZAround.me/fork
.. _Clone: http://git-scm.com/book/en/Git-Basics-Getting-a-Git-Repository#Cloning-an-Existing-Repository
.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation
.. _autoenv: https://github.com/kennethreitz/autoenv
.. _`Install PostGIS for GeoDjango`:
    https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/postgis
.. _`Post-installation`: https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/postgis/#post-installation

Run on Heroku
-------------

#. Install the prerequisites for Heroku.  See
   `Getting Started with Django on Heroku`_ for detailed instructions.
   Get to the point where you've created your app (after ``heroku create``).

.. _`Getting Started with Django on Heroku`:
    https://devcenter.heroku.com/articles/getting-started-with-django

#. Configure your app.  Here's a suggested configuration::

   heroku config:set DJANGO_DEBUG=1
   heroku config:set SECURE_PROXY_SSL_HEADER="HTTP_X_FORWARDED_PROTO,https"
   heroku config:set ALLOWED_HOSTS=*
   heroku config:set INSTALLED_APPS=gunicorn
   heroku config:set STATIC_ROOT=staticfiles
   heroku config:set SECRET_KEY=`openssl rand -base64 32`

#. Push the code to Heroku::

    git push heroku master

#. Run it::

   $ heroku ps:scale web=1
   $ heroku ps    # Verify
   $ heroku open  # Open in your browser, or
   $ heroku logs  # See what went wrong



Make Changes
------------
1. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

2. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox::

    $ make qa-all

3. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

4. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.6, 2.7, 3.3, and 3.4, and for PyPy. Check
   https://travis-ci.org/codefortulsa/BPZAround.me/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

    $ python -m unittest tests.test_BPZAround.me
