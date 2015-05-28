drf-tz-fields
======================================

|build-status-image| |pypi-version|

Overview
--------

Pytz timezone object support for django rest framework serializers and more. Requires
https://github.com/mfogel/django-timezone-field

Requirements
------------

-  Python (3.3, 3.4)
-  Django (1.8)
-  Django REST Framework (3.1) [3.0+ could work, but no being tested]

Installation
------------
NOT ADDED TO PIP YET

Install using ``pip``\ …

.. code:: bash

    $ pip install drf-tz-fields

Example
-------

TODO: Write example.

Testing
-------

Install testing requirements.

.. code:: bash

    $ pip install -r requirements.txt

Run with runtests.

.. code:: bash

    $ ./runtests.py

You can also use the excellent `tox`_ testing tool to run the tests
against all supported versions of Python and Django. Install tox
globally, and then simply run:

.. code:: bash

    $ tox

Documentation
-------------

To build the documentation, you’ll need to install ``mkdocs``.

.. code:: bash

    $ pip install mkdocs

To preview the documentation:

.. code:: bash

    $ mkdocs serve
    Running at: http://127.0.0.1:8000/

To build the documentation:

.. code:: bash

    $ mkdocs build

.. _tox: http://tox.readthedocs.org/en/latest/

.. |build-status-image| image:: https://secure.travis-ci.org/slessans/drf-tz-fields.svg?branch=master
   :target: http://travis-ci.org/slessans/drf-tz-fields?branch=master
.. |pypi-version| image:: https://img.shields.io/pypi/v/drf-tz-fields.svg
   :target: https://pypi.python.org/pypi/drf-tz-fields
