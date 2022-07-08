import connexion
import six
import yaml
import psycopg2
import glob
import os
import csv
import time
import traceback

from cloudharness.workflows import tasks, operations

from pub_chem_index.models.molecule import Molecule  # noqa: E501
from pub_chem_index import util
from pub_chem_index.services import lookup


def get_molecules():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    conn = psycopg2.connect(
        host='pubchem-db',
        port=5432,
        dbname='asu',
        user='mnp',
        password='metacell'
    )
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT * FROM synonyms;
            """)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        traceback.print_exc()
        return 'Error submitting operation: %s' % e, 500

def search_molecules(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: Molecule
    """
    if term.isnumeric():
        return lookup.search_molecules_by_cid(str(term))
    return lookup.search_molecules_by_synonym(str(term))