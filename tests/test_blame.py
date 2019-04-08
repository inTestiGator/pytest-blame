""" Tests the pytest_blame.py plugin for pytest """
import pytest
import pytest_blame


def test_conftest(testdir):
    """Make sure that our plugin works."""
    testdir.makeconftest(
        """
        import pytest
        from git import Repo

        def pytest_addoption(parser):
            group = parser.getgroup("track")
            group.addoption(
                "--track",
                action="store_true",
                help="pytest-blame help \n--track: show last git commit",
            )

        # pylint: disable=E1101
        def pytest_report_header():
            msg = print("Can't find the last passing commit")
            if pytest.config.getoption("track"):
                PATH = "."
                repo = Repo(PATH)
                commits = list(repo.iter_commits())
                msg = print(
                    "\nLast passing commit --> ", commits[0].author, ":", commits[0].message
                )
            return msg
    """
    )
    testdir.makepyfile(
        """
        def test_add():
            assert sample.add(1, 1) == 2
            assert sample.add(0, 1) != 2
    """
    )
    result = testdir.runpytest()
    result.assert_outcomes(passed=2)
