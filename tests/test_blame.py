""" Tests the pytest_blame.py plugin for pytest """

import pytest
import pytest_blame


@pytest.fixture()
def sample_test(testdir):
    """temporal test file"""
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
    """)
    return testdir


def test_getstatus(sample_test):
    """Make sure that our plugin works."""
    result = sample_test.runpytest(​"--track"​)
    assert "Cannot find the last passing commit" in result.stdout
