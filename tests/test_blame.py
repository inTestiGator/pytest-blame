""" Tests the pytest_blame.py plugin for pytest """

import pytest


@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
    """)
    return testdir


def test_addoption():
    """Make sure that our plugin works."""
