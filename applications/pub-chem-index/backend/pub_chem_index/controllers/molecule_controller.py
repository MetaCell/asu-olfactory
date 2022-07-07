import connexion
import six

from pub_chem_index.models.molecule import Molecule  # noqa: E501
from pub_chem_index import util


def get_molecule_by_cid(molecule_by_cid):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param molecule_by_cid: A unique identifier for a &#x60;Molecule&#x60;.
    :type molecule_by_cid: str

    :rtype: Molecule
    """
    return 'do some magic!'


def get_molecule_by_synonym(molecule_by_synonym):  # noqa: E501
    """Get Molecules by synonym.

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param molecule_by_synonym: A unique identifier for a &#x60;Molecule&#x60;.
    :type molecule_by_synonym: str

    :rtype: Molecule
    """
    return 'do some magic!'


def get_molecules():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return 'do some magic!'
