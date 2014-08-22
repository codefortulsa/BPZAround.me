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

Get Started!
------------

Ready to contribute? Here's how to set up `BPZAround.me` for local development.

1. Setup a GeoDjango-compatible database.  We recommend PostgreSQL 9.1+ with
   PostGIS 2.0 or greater.  See these links for help:

   * `PostGIS Installation Page`_
   * `PostgreSQL Download Page`_
   * `Installing PostGIS`_ from Django documentation

.. _`PostGIS Installation Page`: http://postgis.net/install
.. _`PostgreSQL Download Page`: http://www.postgresql.org/download/
.. _`Installing PostGIS`: https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/postgis

2. Create a template PostgreSQL database with the PostGIS extensions loaded.
   This will be used for your development database and for temporary databases
   created during tests::

    $ createdb template_postgis
    $ psql template_postgis -c "CREATE EXTENSION postgis;"
    $ psql template_postgis -c "CREATE EXTENSION postgis_topology;"
    $ psql template_postgis -c "UPDATE pg_database SET datistemplate=true WHERE datname='template_postgis';"


3. Fork the `BPZAround.me` repo on GitHub.
4. Clone your fork locally::

    $ git clone git@github.com:your_name_here/BPZAround.me.git

5. Install your local copy into a virtualenv. Assuming you have
   virtualenvwrapper installed, this is how you set up your fork for local
   development::

    $ mkvirtualenv BPZAround.me
    $ cd BPZAround.me/
    $ pip install -r requirements.txt -r requirements.test.txt -r requirements.dev.txt

6. Setup your local environment::

    $ vi $VIRTUAL_ENV/bin/postactivate  # Add exporting variables
    $ vi $VIRTUAL_ENV/bin/postactivate  # Unset variables
    $ source $VIRTUAL_ENV/bin/postactivate  # Apply changes

   Here's a suggested postactivate::

    #!/bin/bash
    # This hook is run after this virtualenv is activated.

    export DJANGO_DEBUG=1
    export DATABASE_URL=postgis://bpzaroundme@/bpzaroundme

   And the matching predeactivate::

    #!/bin/bash
    # This hook is run after this virtualenv is activated.

    unset DJANGO_DEBUG
    unset DATABASE_URL

   See bpzaroundme/settings.py for additional settings.

7. Get your PostGIS database setup::

    $ createuser --createdb --login bpzaroundme
    $ createdb --owner=bpzaroundme --template=template_postgis bpzaroundme
    $ ./manage.py syncdb  # Setup your superuser as well

8. Make sure tests work::

   $ ./manage.py test

9. Run it!::

   $ ./manage.py runserver


Run on Heroku
-------------

1. Install the prerequisites for Heroku.  See
   `Getting Started with Django on Heroku`_ for detailed instructions.
   Get to the point where you've created your app (after ``heroku create``).

.. _`Getting Started with Django on Heroku`:
    https://devcenter.heroku.com/articles/getting-started-with-django

2. Configure your app.  Here's a suggested configuration::

   $ heroku config
   $ heroku config:set DJANGO_DEBUG=1
   $ heroku config:set SECURE_PROXY_SSL_HEADER="HTTP_X_FORWARDED_PROTO,https"
   $ heroku config:set ALLOWED_HOSTS=*
   $ heroku config:set INSTALLED_APPS=gunicorn
   $ heroku config:set STATIC_ROOT=staticfiles
   $ heroku config:set SECRET_KEY=`python -c "from django.utils.crypto import get_random_string; print(get_random_string())"`

3. Run it::

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
