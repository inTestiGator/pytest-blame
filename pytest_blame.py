import pytest

def pytest_addoption(parser):
    """ Print stuff to header with --track :D """
    group = parser.getgroup('track')
    group.addoption("--track", action="store_true",
                    help="pytest-blame help :D\n--track: show last git commit")


def pytest_report_header():
    """ Display github commit in header """
    if pytest.config.getoption('track'):
        return "User: username Commit: commit Status: FAILING"
