# pytest-blame

![logo](.github/temp-blame-icon.jpg "alt-text")

[![Build Status](https://api.travis-ci.com/inTestiGator/pytest-blame.svg?branch=master)](
https://travis-ci.com/inTestiGator/pytest-blame)
[![codecov.io](http://codecov.io/github/inTestiGator/pytest-blame/coverage.svg?branch=master)](
http://codecov.io/github/inTestiGator/pytest-blame?branch=master)
[![made-with-python](http://img.shields.io/badge/Made%20with-Python-blue.svg)](
https://www.python.org/)
[![PyPI version](https://img.shields.io/pypi/v/pytest-blame.svg)](https://test.pypi.org/project/pytest-blame/)
[![gitter-join-chat](https://badges.gitter.im/Join%20Chat.svg)](
https://gitter.im/pytest-blame/community)

A pytest plugin that helps developers build successful test cases by providing
them with GitHub commit information when their test cases fail.

## Basic Features

After `pytest-blame` has been successfully installed run pytest with
the `--track` flag and you will see a report containing GitHub information at
the top of your pytest report. `pytest-blame` will display the number of test
cases that passed in the latest commit to GitHub, so you can compare it with your
current rate.

To run:
As of now there isn't a way to see the output in a standard way.
To run you need to copy the contents of `pytest_blame.py` over to `tests/conftest.py`

```
cp pytest_blame.py tests/conftest.py
```

then running `pytest --track tests/` to see the output of the plugin.

[Sample PyPI page](https://test.pypi.org/project/pytest-blame/)

Install the most recent version of this plugin with

```
pip install -i https://test.pypi.org/simple/ pytest-blame
```

## Additional Features

Read commits on GitHub and print out information since the most recent commit
that passed test case.
