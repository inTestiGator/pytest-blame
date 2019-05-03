# pytest-blame

![logo](https://raw.githubusercontent.com/inTestiGator/pytest-blame/doc/readme/.github/blame-icon.png)

---

[![Build Status](https://api.travis-ci.com/inTestiGator/pytest-blame.svg?branch=master)](
https://travis-ci.com/inTestiGator/pytest-blame)
[![codecov.io](https://img.shields.io/codecov/c/github/inTestiGator/pytest-blame/master.svg)](
http://codecov.io/github/inTestiGator/pytest-blame?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/891cced8c49c477f8ce46f4532eba718)](https://www.codacy.com/app/wuj/pytest-blame?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=inTestiGator/pytest-blame&amp;utm_campaign=Badge_Grade)
[![made-with-python](http://img.shields.io/badge/Made%20with-Python-blue.svg)](
https://www.python.org/)
[![PyPI version](https://img.shields.io/pypi/v/pytest-blame.svg)](https://pypi.org/project/pytest-blame/)
[<img src="https://img.shields.io/github/release/inTestiGator/pytest-blame.svg" />](https://github.com/inTestiGator/pytest-blame/releases)
[![gitter-join-chat](https://badges.gitter.im/Join%20Chat.svg)](
https://gitter.im/pytest-blame/community)

A pytest plugin that helps developers build successful test cases by providing
them with GitHub commit information when their test cases fail.

## A Python Plugin for Tracking Test Case Status

---

Everyone uses pytest. Or at least, everyone should. It's a super useful testing
program with an easy-to-use syntax. Pytest Blame is a pytest plugin that allows
pytest to do a quick check to Github to make sure the most recent commit is
passing your cases. If somebody broke your cases, ``pytest-blame`` will display
all the commits pushed since the build broke as well as who pushed each commit.
This keeps team workflow transparent and allows for semi-realtime updates from
Github without having to open a browser. Since ``pytest-blame`` can check up on
the online repository as frequently as every time you run your test suite, there
is less risk of a broken commit going unnoticed until a merge conflict occurs.

## Installation

---

To install ``pytest-blame`` you will need to clone this github repository. Once
the repository has been cloned you will need to run the install script to update
your pytest configuration:

```
pipenv run python setup.py install
```

After ``pytest-blame`` has been successfully installed you will need to generate
a Github User Token.

*This can be found under ``Settings`` in your github profile:*

<!-- TODO: 1080p minimum resolution, widescreen gifs -->
<!-- HTML is used here to specify the relative size for the gifs -->
<img src=
"https://raw.githubusercontent.com/inTestiGator/pytest-blame/doc/readme/.github/key1.gif"
     alt="key1 gif"
     width="80%"
     height="80%"/>

<em>Then, find ``Developer Settings`` in the dashboard on the left and navigate to
``Personal Access Tokens``.</em>

<img src=
"https://raw.githubusercontent.com/inTestiGator/pytest-blame/doc/readme/.github/key2.gif"
     alt="key2 gif"
     width="80%"
     height="80%"/>

<em>Finally, when generating the key for ``pytest-blame`` make sure to include
rights to ``repo`` and ``hooks``</em>

<img src=
"https://raw.githubusercontent.com/inTestiGator/pytest-blame/doc/readme/.github/key3.gif"
     alt="key3 gif"
     width="80%"
     height="80%"/>
<!-- -->

Now that you have a user token, you will need to paste it into the location where
your terminal is sourced from. For example: Ubuntu uses ``bash``, so the default
terminal source for ubuntu is ``.bashrc``.

You should put the following code in dot files to set up environment variable:

```shell
export GITHUB_OAUTH_TOKEN = "YOUR_TOKEN"
```

If you are using Windows, you can go to `Control Panel -> System and Security ->
System -> Advanced system settings -> Advanced -> Environment Variables` to
set it up.

## Usage

You can run pytest with the ``--track`` option and you will see a report
containing GitHub information at the top of your pytest report.
``pytest-blame`` will display the most recent commit that is passing CI
check, and all commits that did not pass CI check between the most
recent commit and the most recent passing commit.

To run:
``pytest --track tests/`` will invoke ``pytest-blame``, displaying the current
status of your working branch in the pytest header.

## Sample output

---

A successful ``pytest-blame`` run will look something like this:

```
pytest --track tests/
```

Output:

```
The most recent commit is passing:  https://github.com/inTestiGator/pytest-blame/commit/88ebf4107bc88d247a137d98ec9b45f6ae2658d3
Lancaster Wu : Delete index.md
```

or

```
Most recent passing commit: https://github.com/inTestiGator/pytest-blame/commit/4d4c5cb72cc86cfe35fb19e7630699f405677c69

Patrick Palad: Disable pylint check

--------------------------------
Failing commit: https://github.com/inTestiGator/pytest-blame/commit/9d5d00bc8276d1efefb6beed39186b1bd9c64946
Spencer Huang: return to passing commit

Failing commit: https://github.com/inTestiGator/pytest-blame/commit/03c68b6ff910ab46407c01ce382c7161f5906d43
Spencer Huang: failing commit

Failing commit: https://github.com/inTestiGator/pytest-blame/commit/aab2684e748be41a73213861d1cedc4b5842f81a
Spencer Huang: failling commit

Failing commit: https://github.com/inTestiGator/pytest-blame/commit/4d4c5cb72cc86cfe35fb19e7630699f405677c69
Spencer Huang: fail test

The last one is the most recent commit
```

You may also recieve messages telling you that `can not find passing commits` when
all commits are currently failing or pending.

## Failing Travis build

The master branch is failing Travis because one of our test cases requires
Travis to have access to our test repository and currently and it doesn't,
so it cannot perform the actual testing.

## The Team

Check out the Pytest Blame Team!

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/quigley-c">
      <img src="https://avatars1.githubusercontent.com/u/35495466?s=460&v=4"
        width=128px;>
      <h3>Carson Quigley</h3>
    </td>
    <td align="center">
      <a href="https://github.com/lancasterwu">
      <img src="https://avatars3.githubusercontent.com/u/31478979?s=460&v=4"
        width=128px;>
      <h3>Lancaster Wu</h3>
    </td>
    <td align="center">
      <a href="https://github.com/huangs1">
      <img src="https://avatars3.githubusercontent.com/u/31478964?s=460v=4"
        width=128px;>
      <h3>Spencer Huang</h3>
    </td>
    <td align="center">
      <a href="https://github.com/paladp">
      <img src="https://avatars3.githubusercontent.com/u/31668620?s=460v=4"
        width=128px;>
      <h3>Patrick Palad</h3>
    </td>
    <td align="center">
      <a href="https://github.com/livingstonp729">
      <img src="https://avatars3.githubusercontent.com/u/46819028?s=460&v=4"
        width=128px;>
      <h3>Paul Livingston</h3>
  </tr>
</table>
