# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from pub_chem_index.models.base_model_ import Model
from pub_chem_index import util


class Molecule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cid=None, synonym=None, exact_match=None):  # noqa: E501
        """Molecule - a model defined in OpenAPI

        :param cid: The cid of this Molecule.  # noqa: E501
        :type cid: int
        :param synonym: The synonym of this Molecule.  # noqa: E501
        :type synonym: str
        :param exact_match: The exact_match of this Molecule.  # noqa: E501
        :type exact_match: bool
        """
        self.openapi_types = {
            'cid': int,
            'synonym': str,
            'exact_match': bool
        }

        self.attribute_map = {
            'cid': 'cid',
            'synonym': 'synonym',
            'exact_match': 'exact_match'
        }

        self._cid = cid
        self._synonym = synonym
        self._exact_match = exact_match

    @classmethod
    def from_dict(cls, dikt) -> 'Molecule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Molecule of this Molecule.  # noqa: E501
        :rtype: Molecule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cid(self):
        """Gets the cid of this Molecule.


        :return: The cid of this Molecule.
        :rtype: int
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """Sets the cid of this Molecule.


        :param cid: The cid of this Molecule.
        :type cid: int
        """

        self._cid = cid

    @property
    def synonym(self):
        """Gets the synonym of this Molecule.

        List of synonyms matching search query  # noqa: E501

        :return: The synonym of this Molecule.
        :rtype: str
        """
        return self._synonym

    @synonym.setter
    def synonym(self, synonym):
        """Sets the synonym of this Molecule.

        List of synonyms matching search query  # noqa: E501

        :param synonym: The synonym of this Molecule.
        :type synonym: str
        """

        self._synonym = synonym

    @property
    def exact_match(self):
        """Gets the exact_match of this Molecule.

        Flag true if it matches search exactly  # noqa: E501

        :return: The exact_match of this Molecule.
        :rtype: bool
        """
        return self._exact_match

    @exact_match.setter
    def exact_match(self, exact_match):
        """Sets the exact_match of this Molecule.

        Flag true if it matches search exactly  # noqa: E501

        :param exact_match: The exact_match of this Molecule.
        :type exact_match: bool
        """

        self._exact_match = exact_match
