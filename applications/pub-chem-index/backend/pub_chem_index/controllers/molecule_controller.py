import glob
import os
import csv
import time
import traceback

from pub_chem_index.models.molecule import Molecule  # noqa: E501
from pub_chem_index import util
from pub_chem_index.services import lookup


def get_molecules():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return lookup.get_all_molecules()

def search_molecules(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_molecules_by_cid(term)
    return lookup.search_molecules_by_synonym(term)