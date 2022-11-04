import connexion
import six
from cloudharness.workflows import tasks, operations
from pub_chem_index import util

INGESTION_FILES = [
    "CID-MeSH",
    "CID-Synonym-filtered.gz",
    "CID-IUPAC.gz",
    "CID-InChI-Key.gz",
    "CID-Title.gz",
    "CID-SMILES.gz",
    "CID-Synonym-unfiltered.gz",
    "CID-Component.gz",
    "CID-Parent.gz",
    "CID-Patent.gz",
    "CID-PMID.gz",
    "CID-Mass.gz",
    "CID-PMID.gz",
    "CID-SID.gz"
]

def ingest():  # noqa: E501
    """ingest

     # noqa: E501


    :rtype: str
    """
    shared_directory = '/data/db'
    ingestion_tasks = []
    for ingestion_file in INGESTION_FILES:
        ingestion_tasks.append(
            tasks.CustomTask(
                f'ingest-{ingestion_file.lower().split(".")[0]}',
                'pub-chem-index-ingestion',
                shared_directory=shared_directory,
                filename=f"{ingestion_file}"
            )
        )

    # to ingest all files sequential replace the parallel op with a pipeline op
    # op = operations.PipelineOperation(

    # ingest all files parallel
    op = operations.ParallelOperation(
        f'ingest-data', tuple(ingestion_tasks),
        shared_directory=shared_directory,
        shared_volume_size=64000 # 64Gi
    )
    op.execute()
    return "Ingesting Data"

#
