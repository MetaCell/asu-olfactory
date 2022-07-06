import connexion
import six
from cloudharness.workflows import tasks, operations
from pub_chem_index import util


def ingest():  # noqa: E501
    """ingest

     # noqa: E501


    :rtype: str
    """
    shared_directory = 'pubchem-db:/data/db/pgdata'
    task_ingest = tasks.CustomTask('ingest', 'pub-chem-index-ingestion')

    op = operations.PipelineOperation(
        'ingest-data-', (task_ingest, ), shared_directory=shared_directory)
    op.execute()
    return "OK"
