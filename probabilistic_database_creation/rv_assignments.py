import string

from database.fetch_data import *

from database.fetch_data import *
def generate_rvs(table_name,dependent_attributes):
    dependent_attributes_mappings = []
    for attribute in dependent_attributes:
        attribute_tuples = fetch_data_results(find_distinct_attribute_values(table_name,attribute))
        distinct_attribute_values = [attribute_tuple[0] for attribute_tuple in attribute_tuples]
        rvs = {}
        for i, name in enumerate(distinct_attribute_values):
            rvs[i+1] = name
        dependent_attributes_mappings.append(rvs)
    return dependent_attributes_mappings


def create_rv_assignments(dependent_attributes_mappings,table_name,determinant_attributes):
    determinant_tuples = fetch_data_results(find_distinct_attribute_values(table_name,determinant_attributes[0]))
    distinct_determinant_values = [determinant_tuple[0] for determinant_tuple in determinant_tuples]
    rv_assignments = {}
    for i, determinant in enumerate(distinct_determinant_values):
        rv_assignment = {}
        for dependent, letter in zip(dependent_attributes_mappings, string.ascii_lowercase):
            for key,value in dependent.items():
                rv_assignment[f'{letter}{i+1}={key}'] = value
        rv_assignments[determinant] = rv_assignment
    return rv_assignments