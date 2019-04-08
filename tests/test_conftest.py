""" Tests the conftest.py plugin for pytest """


def test_conftest(testdir, capsys):
    """Make sure that our plugin works."""
    testdir.makeconftest(
        """
import pytest
from git import Repo

def pytest_addoption(parser):
    group = parser.getgroup('track')
    group.addoption(
        '--track',
        action='store_true',
        help='--track: show last git commit',
        )

def pytest_report_header():
    msg = print('Cannot find the last passing commit')
    if pytest.config.getoption('track'):
        PATH = '.'
        repo = Repo(PATH)
        commits = list(repo.iter_commits())
        msg = print(
            'Last passing commit --> ', commits[0].author, ':', commits[0].message
        )
    return msg
"""
    )
    testdir.makepyfile(
        """
def add(a, b):
    return a + b

def test_add():
    assert add(1, 1) == 2
    assert add(0, 1) != 2
"""
    )
    testdir.runpytest()
    standard_out, standard_err = capsys.readouterr()
    assert "Cannot find the last passing commit" in standard_out
    assert standard_err == ""
