# pytest-blame

![logo](temp-blame-icon.jpg "alt-text")

[![Build Status](https://api.travis-ci.org/inTestiGator/pytest-blame.svg?branch=master)](
https://travis-ci.org/inTestiGator/pytest-blame)
[![codecov.io](http://codecov.io/github/inTestiGator/pytest-blame/coverage.svg?branch=master)](
http://codecov.io/github/inTestiGator/pytest-blame?branch=master)
[![made-with-python](http://img.shields.io/badge/Made%20with-Python-orange.svg)](
https://www.python.org/)

A pytest plugin that helps developers build succesful test cases by providing
them with GitHub commit information when their test cases fail.

## Basic Features

After `pytest-blame` has been successfully installed run pytest with
the `--track` flag and you will see a report containing GitHub information at
the top of your pytest report. `pytest-blame` will display the number of test
cases that passed in the latest commit to GitHub, so you can compare it with your
current rate.

<<<<<<< HEAD
=======
To run:
As of now there isn't a way to test in a standard way.
To test I am copying the contents of `pytest_blame.py` over to `tests/conftest.py`

```
cp pytest_blame.py tests/conftest.py
```

then running `pytest --track tests/` to see the output of the plugin.

>>>>>>> 34a8974fb793417709a5143c47eb69e33f586837
## Additional Features

Read commits on GitHub and print out information since the most recent commit
that passed test case.
