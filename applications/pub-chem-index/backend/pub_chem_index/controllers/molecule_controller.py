import glob
import os
import csv
import time
import traceback
from pub_chem_index.models.molecule import Molecule  # noqa: E501
from pub_chem_index.models.molecule_inchi import MoleculeInchi  # noqa: E501
from pub_chem_index import util
from pub_chem_index.services import lookup


def get_inchi():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[MoleculeInchi]
    """
    return lookup.get_all_values('cid_inchi_key')


def get_mesh():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return lookup.get_all_values('cid_mesh')


def get_smiles():  # noqa: E501
    """List All Smiles

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return lookup.get_all_values('cid_smiles')


def get_synonyms():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return lookup.get_all_values('cid_synonym_filtered')


def get_title():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return lookup.get_all_values('cid_title')


def get_iupac():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return lookup.get_all_values('cid_iupac')


def search_inchi(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[MoleculeInchi]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_inchi_key', term)
    return lookup.search_table_by_value('cid_inchi_key', 'inchi' ,term)



def search_mesh(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_mesh', term)
    return lookup.search_table_by_value('cid_mesh', 'mesh' ,term)



def search_smiles(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_smiles', term)
    return lookup.search_table_by_value('cid_smiles', 'smiles' ,term)



def search_synonyms(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_synonym_filtered', term)
    return lookup.search_table_by_value('cid_synonym_filtered', 'Synonym' ,term)


def search_title(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_title', term)
    return lookup.search_table_by_value('cid_title', 'title' ,term)


def search_iupac(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_iupac', term)
    return lookup.search_table_by_value('cid_iupac', 'iupac' ,term)
