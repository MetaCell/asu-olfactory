import glob
import os
import csv
import time
import traceback
import logging
import difflib
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

def get_sid():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return lookup.get_all_values('cid_sid')

def get_pmid():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return lookup.get_all_values('cid_pmid')

def get_mass():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return lookup.get_all_values('cid_mass')

def get_component():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return lookup.get_all_values('cid_component')

def get_parent():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return lookup.get_all_values('cid_parent')

def get_patent():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return lookup.get_all_values('cid_patent')

def get_synonyms_unfiltered():  # noqa: E501
    """List All Molecules

    Gets a list of all &#x60;Molecule&#x60; entities. # noqa: E501


    :rtype: List[Molecule]
    """
    return lookup.get_all_values('cid_synonym_unfiltered')

def exact_match_results(results, term):
    for i, t in enumerate(results):
        if t[1] == term:
            results[i] = t[0], t[1], True
        else:
            results[i] = t[0], t[1], False

    return results

def search_inchi(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[MoleculeInchi]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_inchi_key', term)

    results = lookup.search_table_by_value('cid_inchi_key', 'inchi' ,term)

    results = exact_match_results(results, term)

    return sorted(results, key = lambda t : (t[1], t[2]))

def search_mesh(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_mesh', term)

    results = lookup.search_table_by_value('cid_mesh', 'mesh' ,term)

    results = exact_match_results(results, term)

    return sorted(results, key = lambda t : (t[1], t[2]))


def search_smiles(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_smiles', term)

    results = lookup.search_table_by_value('cid_smiles', 'smiles' ,term)
    
    results = exact_match_results(results, term)

    return sorted(results, key = lambda t : (t[1], t[2]))

def search_synonyms(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_synonym_filtered', term)

    results = lookup.search_table_by_value('cid_synonym_filtered', 'Synonym' ,term)
    
    results = exact_match_results(results, term)

    return sorted(results, key = lambda t : (t[1], t[2]))

def search_title(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_title', term)
    
    results = lookup.search_table_by_value('cid_title', 'title' ,term)
    
    results = exact_match_results(results, term)

    return sorted(results, key = lambda t : (t[1], t[2]))

def search_iupac(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_iupac', term)

    results = lookup.search_table_by_value('cid_iupac', 'iupac' ,term)
    
    results = exact_match_results(results, term)

    return sorted(results, key = lambda t : (t[1], t[2]))

def search_pmid(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_pmid', term)

    results = lookup.search_table_by_value('cid_pmid', 'pmid' ,term)

    results = exact_match_results(results, term)

    return sorted(results, key = lambda t : (t[1], t[2]))

def search_sid(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_sid', term)

    results = lookup.search_table_by_value('cid_sid', 'sid' ,term)

    results = exact_match_results(results, term)

    return sorted(results, key = lambda t : (t[1], t[2]))

def search_mass(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_mass', term)

    results = lookup.search_table_by_value('cid_mass', 'molecule' ,term)

    results = exact_match_results(results, term)

    return sorted(results, key = lambda t : (t[1], t[2]))

def search_component(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_component', term)

    results = lookup.search_table_by_value('cid_component', 'component' ,term)

    results = exact_match_results(results, term)

    return sorted(results, key = lambda t : (t[1], t[2]))

def search_patent(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_patent', term)

    results = lookup.search_table_by_value('cid_patent', 'patent' ,term)

    results = exact_match_results(results, term)

    return sorted(results, key = lambda t : (t[1], t[2]))

def search_parent(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_parent', term)

    results = lookup.search_table_by_value('cid_parent', 'parent' ,term)

    results = exact_match_results(results, term)

    return sorted(results, key = lambda t : (t[1], t[2]))

def search_synonyms_unfiltered(term):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param term: A unique identifier for a &#x60;Molecule&#x60;.
    :type term: str

    :rtype: List[Molecule]
    """
    if term.isnumeric():
        return lookup.search_table_by_cid('cid_synonym_unfiltered', term)

    results = lookup.search_table_by_value('cid_synonym_unfiltered', 'Synonym' ,term)

    results = exact_match_results(results, term)

    return sorted(results, key = lambda t : (t[1], t[2]))

def join_results(table_name, column_name, term, properties):
    tables_list = properties.split(',')
    logging.info("List of Tables %s", properties)
    logging.info("List of Tables %s", tables_list)

    first_results = []
    if term.isnumeric():
        first_results = lookup.search_table_by_cid(table_name, term)
    else:
        first_results = lookup.search_table_by_value(table_name, column_name ,term)

    first_results = sorted(exact_match_results(first_results, term), key = lambda t : (t[1], t[2]))

    results = []
    for i, t in enumerate(first_results):
        result = {}
        result["cid"] = t[0]
        result[table_name] = t[1]
        logging.info("Looking at %s", t[0])
        for table in tables_list:
            table_results = lookup.search_table_by_cid(table, int(t[0]))
            logging.info("Looking at table %s", table)
            for t in enumerate(table_results):
                t[1].pop(0)
                result[table] = t[1]
        results.append(result)
        logging.info("Looking at result %s", result)

    return results

def search_across_tables(cids, tables):  # noqa: E501
    """Get a Molecule

    Gets the details of a single instance of a &#x60;Molecule&#x60;. # noqa: E501

    :param cids: List of cids.
    :type cids: str
    :param tables: List of tables
    :type tables: str

    :rtype: List[Molecule]
    """
    cids_list = cids.split(',')
    tables_list = tables.split(',')
    logging.info("List of CIDS %s", cids)
    logging.info("List of Tables %s", tables)

    logging.info("List of CIDS %s", cids_list)
    logging.info("List of Tables %s", tables_list)
    results = []
    for cid in cids_list:
        result = {}
        result["cid"] = cid
        logging.info("Looking at %s", cid)
        for table in tables_list:
            table_results = lookup.search_table_by_cid(table, cid)
            logging.info("Looking at table %s", table)
            for t in enumerate(table_results):
                result[table] = t[1]
        results.append(result)
    return results

def search_synonyms_properties(term, tables):  # noqa: E501
    results = join_results("cid_synonym_filtered", "synonym", term, tables);
   
    return results

def search_synonyms_unfiltered_properties(term, tables):  # noqa: E501
    results = join_results("cid_synonym_unfiltered", "synonym", term, tables);
   
    return results

def search_sid_properties(term, tables):  # noqa: E501
    results = join_results("cid_sid", "sid", term, tables);
   
    return results

def search_pmid_properties(term, tables):  # noqa: E501
    results = join_results("cid_pmid", "pmid", term, tables);
   
    return results
    
def search_smiles_properties(term, tables):  # noqa: E501
    results = join_results("cid_smiles", "smiles", term, tables);
   
    return results

def search_component_properties(term, tables):  # noqa: E501
    results = join_results("cid_component", "component", term, tables);
   
    return results

def search_title_properties(term, tables):  # noqa: E501
    results = join_results("cid_title", "title", term, tables);
   
    return results    

def search_mesh_properties(term, tables):  # noqa: E501
    results = join_results("cid_mesh", "mesh", term, tables);
   
    return results

def search_iupac_properties(term, tables):  # noqa: E501
    results = join_results("cid_iupac", "iupac", term, tables);
   
    return results

def search_inchi_properties(term, tables):  # noqa: E501
    results = join_results("cid_inchi_key", "inchi", term, tables);
   
    return results

def search_parent_properties(term, tables):  # noqa: E501
    results = join_results("cid_parent", "parent", term, tables);
   
    return results

def search_patent_properties(term, tables):  # noqa: E501
    results = join_results("cid_patent", "patent", term, tables);
   
    return results

def search_mass_properties(term, tables):  # noqa: E501
    results = join_results("cid_mass", "molecule", term, tables);
   
    return results