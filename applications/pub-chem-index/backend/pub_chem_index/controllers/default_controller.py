import connexion
import six
from cloudharness.workflows import tasks, operations
from pub_chem_index import util


def ingest():  # noqa: E501
    """ingest

     # noqa: E501


    :rtype: str
    """
    shared_directory = 'pubchem-db:/data/db'
    task_ingest = tasks.CustomTask('ingest', 'pub-chem-index-ingestion', shared_directory=shared_directory)

    op = operations.PipelineOperation(
        'ingest-data-', (task_ingest, ), shared_directory=shared_directory)
    execute = op.execute()
    return "Ingesting Data"
