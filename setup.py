from setuptools import setup, find_packages
from say_what._version import __version__

setup(
    name = 'say_what.py',
    packages = find_packages(),
    author = 'The Mayo Clinic Neurology AI Program',
    version = __version__,
)