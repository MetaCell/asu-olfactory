import operator

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

def exact_match_results(results, term, include_cid):
    for i, t in enumerate(results):
        if include_cid is True:
            if t[1] == term:
                results[i] = t[0], t[1], True
            else:
                results[i] = t[0], t[1], False
        if include_cid is False:
            if t[1] == term:
                results[i] = t[1], True
            else:
                results[i] = t[1], False

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

    results = exact_match_results(results, term, True)

    return sorted(results, key = lambda t : (t[2]), reverse=True)

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

    results = exact_match_results(results, term, True)

    return sorted(results, key = lambda t : (t[2]), reverse=True)


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
    
    results = exact_match_results(results, term, True)

    return sorted(results, key = lambda t : (t[2]), reverse=True)

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
    
    results = exact_match_results(results, term, True)

    return sorted(results, key = lambda t : (t[2]), reverse=True)

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
    
    results = exact_match_results(results, term, True)

    return sorted(results, key = lambda t : (t[2]), reverse=True)

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
    
    results = exact_match_results(results, term, True)

    return sorted(results, key = lambda t : (t[2]), reverse=True)

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

    results = exact_match_results(results, term, True)

    return sorted(results, key = lambda t : (t[2]), reverse=True)

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

    results = exact_match_results(results, term, True)

    return sorted(results, key = lambda t : (t[2]), reverse=True)

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

    results = exact_match_results(results, term, True)

    return sorted(results, key = lambda t : (t[2]), reverse=True)

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

    results = exact_match_results(results, term, True)

    return sorted(results, key = lambda t : (t[2]), reverse=True)

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

    results = exact_match_results(results, term, True)

    return sorted(results, key = lambda t : (t[2]), reverse=True)

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

    results = exact_match_results(results, term, True)

    return sorted(results, key = lambda t : (t[2]), reverse=True)

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

    results = exact_match_results(results, term, True)

    return sorted(results, key = lambda t : (t[2]), reverse=True)

def join_results(table_name, column_name, term, properties):
    tables_list = properties.split(',')

    for index, table in enumerate(tables_list):
        tables_list[index] = "cid_ " + table

    first_results = []
    if term.isnumeric():
        first_results = lookup.search_table_by_cid(table_name, term)
    else:
        first_results = lookup.search_table_by_value(table_name, column_name ,term)

    first_results = sorted(exact_match_results(first_results, term, True), key = lambda t : (t[2]), reverse=True)

    results = []
    tables = {}
    for i, t in enumerate(first_results):
        result = {}
        result["cid"] = t[0]
        exact = False
        if term == t[1]:
            exact = True
        result["exact"] = exact
        result[table_name.replace("cid_", "")] = t[1]
        for table in tables_list:
            if table not in tables:
                table_results = lookup.search_table_by_cid(table, t[0])
                tables[table] = sorted(exact_match_results(table_results, term, False), key = lambda t : (t[1]), reverse=True)
            result[table] = tables[table]
        results.append(result)

    return sorted(results.values(), key=operator.attrgetter('exact'), reverse=True)

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