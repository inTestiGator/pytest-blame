
pytest-blame
============


.. image:: .github/temp-blame-icon.jpg
   :target: .github/temp-blame-icon.jpg
   :alt: logo


`
.. image:: https://api.travis-ci.com/inTestiGator/pytest-blame.svg?branch=master
   :target: https://api.travis-ci.com/inTestiGator/pytest-blame.svg?branch=master
   :alt: Build Status
 <https://travis-ci.com/inTestiGator/pytest-blame>`_
`
.. image:: http://codecov.io/github/inTestiGator/pytest-blame/coverage.svg?branch=master
   :target: http://codecov.io/github/inTestiGator/pytest-blame/coverage.svg?branch=master
   :alt: codecov.io
 <http://codecov.io/github/inTestiGator/pytest-blame?branch=master>`_
`
.. image:: http://img.shields.io/badge/Made%20with-Python-blue.svg
   :target: http://img.shields.io/badge/Made%20with-Python-blue.svg
   :alt: made-with-python
 <https://www.python.org/>`_

.. image:: https://img.shields.io/pypi/v/pytest-blame.svg
   :target: https://test.pypi.org/project/pytest-blame/
   :alt: PyPI version

`
.. image:: https://badges.gitter.im/Join%20Chat.svg
   :target: https://badges.gitter.im/Join%20Chat.svg
   :alt: gitter-join-chat
 <https://gitter.im/pytest-blame/community>`_

A pytest plugin that helps developers build successful test cases by providing
them with GitHub commit information when their test cases fail.

Basic Features
--------------

After ``pytest-blame`` has been successfully installed run pytest with
the ``--track`` flag and you will see a report containing GitHub information at
the top of your pytest report. ``pytest-blame`` will display the number of test
cases that passed in the latest commit to GitHub, so you can compare it with your
current rate.

To run:
As of now there isn't a way to see the output in a standard way.
To run you need to copy the contents of ``pytest_blame.py`` over to ``tests/conftest.py``

.. code-block::

   cp pytest_blame.py tests/conftest.py

then running ``pytest --track tests/`` to see the output of the plugin.

`Sample PyPI page <https://test.pypi.org/project/pytest-blame/>`_

Install the most recent version of this plugin with

.. code-block::

   pip install -i https://test.pypi.org/simple/ pytest-blame

Additional Features
-------------------

Read commits on GitHub and print out information since the most recent commit
that passed test case.
