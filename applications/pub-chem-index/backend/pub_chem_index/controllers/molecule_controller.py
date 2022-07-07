import connexion
import six
import yaml

from cloudharness.workflows import tasks, operations

from pub_chem_index.models.molecule import Molecule  # noqa: E501
from pub_chem_index import util


def get_molecules():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    task_search = tasks.CustomTask('search', 'pub-chem-index-search', env_variable1="")

    op = operations.PipelineOperation(
        'search-data-', (task_search))
    execute = op.execute()
    print(execute)
    return "Molecules found"

def get_molecules_by_cid(cid):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param cid: A unique identifier for a &#x60;Molecule&#x60;.
    :type cid: str

    :rtype: Molecule
    """
    print("Searching cid ", cid)
    task_search = tasks.CustomTask('search', 'pub-chem-index-search', env_variable1=cid)

    op = operations.PipelineOperation(
        'search-data-', (task_search))
    execute = op.execute()
    print(execute)
    return "Molecules found"


def get_molecules_by_synonym(synonym):  # noqa: E501
    """Get Molecules by synonym.

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param synonym: A unique identifier for a &#x60;Molecule&#x60;.
    :type synonym: str

    :rtype: Molecule
    """
    def f(synonym):
        import time
        time.sleep(2)
        print('whatever')
        print(synonym)

    task_search = tasks.PythonTask('my-task', f(synonym))

    op = operations.DistributedSyncOperation(
        'search-data-', (task_search))
    print('\n', yaml.dump(op.to_workflow()))
    execute = op.execute()
    print(execute)
    return execute
