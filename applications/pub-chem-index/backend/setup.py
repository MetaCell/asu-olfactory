# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "pub_chem_index"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0",
    "psycopg2-binary"
]

setup(
    name=NAME,
    version=VERSION,
    description="pub_chem_index",
    author_email="cloudharness@metacell.us",
    url="",
    keywords=["OpenAPI", "pub_chem_index"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['pub_chem_index=pub_chem_index.__main__:main']},
    long_description="""\
    pub_chem_index
    """
)

