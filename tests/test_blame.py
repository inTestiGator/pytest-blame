""" Tests the pytest_blame.py plugin for pytest """

import subprocess
import os
import pytest

# pylint: disable=W0621
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


def test_addoption(sample_test):
    """test addoption"""
    os.chdir(f"{os.environ['HOME']}/.local")
    subprocess.run(["git", "clone", "git@github.com:inTestiGator/test-repository.git"])
    os.chdir(f"{os.environ['HOME']}/.local/test-repository/")
    result = sample_test.runpytest("--track")
    print(result.stdout)
    result.stdout.fnmatch_lines(["*"])
    print(result.ret)
    assert result.ret == 5
