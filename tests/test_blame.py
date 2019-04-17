""" Tests the pytest_blame.py plugin for pytest """

import pytest


@pytest.fixture()
def sample_test(testdir):
    """temporal test file"""
    testdir.makepyfile(
        """
        def test_pass():
            assert 1 == 1
    """
    )
    return testdir


def test_addoption(testdir):
    """test addoption"""
    testdir.copy_example("tests/test_sample.py")
    result = testdir.runpytest("--track")
    result.stdout.fnmatch_lines(["*"])
    assert result.ret == 4
