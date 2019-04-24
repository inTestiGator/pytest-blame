"""This file is used to deploy the plugin"""
import io
import os
from setuptools import setup

install_requires = ["pygithub", "pytest>=4.4.0", "gitpython", "requests"]


def read(filename):
    """This function takes in a filepath and reads the file"""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with io.open(filepath, mode="r", encoding="utf-8") as f:
        return f.read()


setup(
    name="pytest-blame",
    version="0.1.6",
    description="A pytest plugin helps developers to debug by providing useful commits history.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Lancaster Wu, Spencer Huang, Carson Quigley, Patrick Palad, Paul Livingston",
    author_email="wuj@allegheny.edu, huangs@allegheny.edu, quigleyc@allegheny.edu, "
    + "paladp@allegheny.edu, livingstonp@allegheny.edu",
    url="https://github.com/inTestiGator/pytest-blame",
    license="GNU",
    platforms="any",
    install_requires=install_requires,
    py_modules=["pytest_blame"],
    entry_points={"pytest11": ["blame = pytest_blame"]},
)
