import connexion
import six
from cloudharness.workflows import tasks, operations

from pub_chem_index.models.molecule import Molecule  # noqa: E501
from pub_chem_index import util


def get_molecules():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    task_search = tasks.CustomTask('search', 'pub-chem-index-search', env_variable1="")

    op = operations.SingleTaskOperation(
        'search-data-', (task_search))
    execute = op.execute()
    return execute

def get_molecules_by_cid(cid):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param cid: A unique identifier for a &#x60;Molecule&#x60;.
    :type cid: str

    :rtype: Molecule
    """
    print("Searching cid ", cid)
    task_search = tasks.CustomTask('search', 'pub-chem-index-search', env_variable1=cid)

    op = operations.SingleTaskOperation(
        'search-data-', (task_search))
    execute = op.execute()
    return execute


def get_molecules_by_synonym(synonym):  # noqa: E501
    """Get Molecules by synonym.

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param synonym: A unique identifier for a &#x60;Molecule&#x60;.
    :type synonym: str

    :rtype: Molecule
    """
    print("Searching synonym ", synonym)
    task_search = tasks.CustomTask('search', 'pub-chem-index-search', env_variable1=synonym)

    op = operations.SingleTaskOperation(
        'search-data-', (task_search))
    execute = op.execute()
    return execute
