import connexion
import six

from pub_chem_index.models.molecule import Molecule  # noqa: E501
from pub_chem_index import util




def create_molecule(molecule):  # noqa: E501
    """Create a Molecule

    Creates a new instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param molecule: A new &#x60;Molecule&#x60; to be created.
    :type molecule: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        molecule = Molecule.from_dict(connexion.request.get_json())  # noqa: E501

    
    return 'do some magic!'


def delete_molecule(molecule_id):  # noqa: E501
    """Delete a Molecule

    Deletes an existing &#x60;Molecule&#x60;. # noqa: E501

    :param molecule_id: A unique identifier for a &#x60;Molecule&#x60;.
    :type molecule_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_molecule(molecule_id):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param molecule_id: A unique identifier for a &#x60;Molecule&#x60;.
    :type molecule_id: str

    :rtype: Molecule
    """
    return 'do some magic!'


def get_molecules():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return 'do some magic!'


def update_molecule(molecule_id, molecule):  # noqa: E501
    """Update a Molecule

    Updates an existing &#x60;Molecule&#x60;. # noqa: E501

    :param molecule_id: A unique identifier for a &#x60;Molecule&#x60;.
    :type molecule_id: str
    :param molecule: Updated &#x60;Molecule&#x60; information.
    :type molecule: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        molecule = Molecule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
