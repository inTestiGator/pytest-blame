""" Tests the pytest_blame.py plugin for pytest """

import pytest


@pytest.fixture()
def sample_test(testdir):
    """temporal test file"""
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
    """)
    return testdir


def test_plugin(testdir):
    testdir.copy_example("tests/test_sample.py")
    testdir.runpytest("--track", "test_sample")


def test_sample():
    pass
