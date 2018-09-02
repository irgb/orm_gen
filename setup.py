import os
import sys
from setuptools import setup, find_packages
from ormgen import get_version

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name         = 'ormgen',
    version      = get_version(),
    packages     = find_packages(),
    install_requires = ['PyMySQL>=0.7.11'],
    entry_points = {
            'console_scripts': [
                'ormgen = ormgen.main:main',
                ]
        },
    url          = 'https://github.com/irgb/ormgen',
    description  = 'generate sqlalchemy orm class automatically from existing database',
    long_description = read('README.rst'),
)
