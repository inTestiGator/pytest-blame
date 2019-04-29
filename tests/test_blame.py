""" Tests the pytest_blame.py plugin for pytest """

import pytest
import subprocess


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
    # testdir.copy_example("tests/test_sample.py")
    subprocess.Popen(['git', 'clone', "git@github.com:inTestiGator/test-repository.git", '$HOME/local'])
    result = sample_test.runpytest("--track $HOME/local/test-repository")
    print(result.stdout)
    result.stdout.fnmatch_lines(["*"])
    assert result.ret == 3
