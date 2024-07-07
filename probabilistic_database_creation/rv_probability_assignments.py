import string
from itertools import product


#Used to generate the possible RVs based on the dependent attributes
#Example -  FD: person -> {model,color}
#determinant attributes passed: ['model','color']
#data = dataframe for inconsistent DB
def generate_rvs(data,dependent_attributes):
    dependent_attributes_mappings = []
    for attribute in dependent_attributes:
        distinct_attribute_values = data[attribute].unique()
        rvs = {}
        for i, name in enumerate(distinct_attribute_values):
            rvs[i+1] = name
        dependent_attributes_mappings.append(rvs)
    return dependent_attributes_mappings


def create_rv_assignments(data,dependent_attributes_mappings,determinant_attributes):
    distinct_determinant_values = data[determinant_attributes[0]].unique()
    rv_assignments = {}
    for i, determinant in enumerate(distinct_determinant_values):
        rv_assignment = {}
        for dependent, letter in zip(dependent_attributes_mappings, string.ascii_lowercase):
            for key,value in dependent.items():
                assignment = {'value': f'{value}', 'prob': 0}
                rv_assignment[f'{letter}{i+1}={key}'] = assignment
        rv_assignments[determinant] = rv_assignment
    return rv_assignments


#RV assignments and Probability calculation for CWA
def create_rv_assignments_with_prob_CWA(data,dependent_attributes_mappings,determinant_attributes,dependent_attributes):
    distinct_determinant_values = data[determinant_attributes[0]].unique()
    rv_assignments = {}
    for i, determinant in enumerate(distinct_determinant_values):
        rv_assignment = []
        owns = data[data[f'{determinant_attributes[0]}']==f'{determinant}']
        for j, (dependent, letter) in enumerate(zip(dependent_attributes_mappings, string.ascii_lowercase)):
            attributes_present = list(set(owns[f'{dependent_attributes[j]}'].tolist()))
            rv_list = {}
            for key,value in dependent.items():
                prob = 0
                if value in attributes_present:
                    #In CWA, all attributes present in the tuple get equal probability
                    #Not present get 0 prob
                    prob = 1/len(attributes_present)
                assignment = {'value': f'{value}', 'prob': prob}
                rv_list[f'{letter}{i+1}={key}'] = assignment
            rv_assignment.append(rv_list)
        rv_assignments[determinant] = rv_assignment
    return rv_assignments


def check_if_already_consistent(owns):
    if owns.shape[0] == 1:
        return True
    else:
        return False

def create_rv_assignments_with_prob_SWA(data,dependent_attributes_mappings,determinant_attributes,dependent_attributes):
    distinct_determinant_values = data[determinant_attributes[0]].unique()
    rv_assignments = {}
    for i, determinant in enumerate(distinct_determinant_values):
        rv_assignment = []
        owns = data[data[f'{determinant_attributes[0]}']==f'{determinant}']
        consistent = check_if_already_consistent(owns)
        for j, (dependent, letter) in enumerate(zip(dependent_attributes_mappings, string.ascii_lowercase)):
            attributes_present = list(set(owns[f'{dependent_attributes[j]}'].tolist()))
            rv_list = {}
            for key,value in dependent.items():
                #Inconsistent and all values possible are present. They get equal prob
                if (value in attributes_present) and (not consistent) and (len(dependent)==len(attributes_present)):
                    prob = 1/len(attributes_present)
                #Inconsistent, but value is present in tuple - 0.8 prob
                elif (value in attributes_present) and (not consistent):
                    prob = 0.8/len(attributes_present)
                elif (value in attributes_present) and (consistent):
                    prob = 1
                elif (value not in attributes_present) and (consistent):
                    prob = 0
                #Inconsistent and value not present in tuple as well
                #0.2 is divided between all such values
                else:
                    prob = 0.2/((len(dependent))-len(attributes_present))
                assignment = {'value': f'{value}', 'prob': prob}
                rv_list[f'{letter}{i + 1}={key}'] = assignment
            rv_assignment.append(rv_list)
        rv_assignments[determinant] = rv_assignment
    return rv_assignments


def compute_sentences(rv_assignments,data,determinant_attributes):
    sentence = {}
    for determinant, assignment in rv_assignments.items():
        lists = [tuple(determinant_dict.items()) for determinant_dict in assignment]
        cartesian_product = []
        owns = data[data[f'{determinant_attributes[0]}'] == f'{determinant}']
        consistent = check_if_already_consistent(owns)
        for combination in product(*lists):
            values = []
            keys = []
            prob = 1
            for item in combination:
                key = item[0]  # Extract the key (e.g., 'a1=1', 'b1=1')
                value_dict = item[1]  # Extract the corresponding dictionary {'value': ..., 'prob': ...}
                values.append(value_dict['value'])  # Append 'value' from each dictionary
                prob = prob and value_dict['prob']
                if (consistent and value_dict['prob'] == 1) or (not consistent):
                    keys.append(key)  # Append key to keys list
            if prob != 0:
                keys_str = ' & '.join(keys)
                cartesian_product.append((tuple(values), keys_str))

        sentence[f'{determinant}'] = cartesian_product
    return sentence
