""" This file is used for deployment. """
import io
import os
from setuptools import setup, find_packages


def read(filename):
    """ This function is reads in the file with the file path """
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with io.open(filepath, mode="r", encoding="utf-8") as f:
        return f.read()


setup(
    name="pytest-blame",
    version="1.0.0",
    description="A pytest plugin helps developers to debug by providing useful commits history.",
    long_description=read("README.md"),
    author="Lancaster Wu, Spencer Huang, Carson Quigley, Patrick Palad, Paul Livingston",
    author_email="wuj@allegheny.edu, huangs@allegheny.edu, quigleyc@allegheny.edu, "
    + "paladp@allegheny.edu, livingstonp@allegheny.edu",
    url="https://github.com/inTestiGator/pytest-blame",
    license="GNU",
    platforms="any",
    packages=find_packages(),
    install_requires=read("requirements.txt").splitlines(),
)
