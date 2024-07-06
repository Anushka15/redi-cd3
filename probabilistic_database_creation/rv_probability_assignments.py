import string

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

def create_rv_assignments_with_prob_CWA(data,dependent_attributes_mappings,determinant_attributes,dependent_attributes):
    distinct_determinant_values = data[determinant_attributes[0]].unique()
    rv_assignments = {}
    for i, determinant in enumerate(distinct_determinant_values):
        rv_assignment = {}
        owns = data[data[f'{determinant_attributes[0]}']==f'{determinant}']
        for j, (dependent, letter) in enumerate(zip(dependent_attributes_mappings, string.ascii_lowercase)):
            attributes_present = list(set(owns[f'{dependent_attributes[j]}'].tolist()))
            for key,value in dependent.items():
                prob = 0
                if value in attributes_present:
                    prob = 1/len(attributes_present)
                assignment = {'value': f'{value}', 'prob': prob}
                rv_assignment[f'{letter}{i+1}={key}'] = assignment
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
        rv_assignment = {}
        owns = data[data[f'{determinant_attributes[0]}']==f'{determinant}']
        consistent = check_if_already_consistent(owns)
        for j, (dependent, letter) in enumerate(zip(dependent_attributes_mappings, string.ascii_lowercase)):
            attributes_present = list(set(owns[f'{dependent_attributes[j]}'].tolist()))
            for key,value in dependent.items():
                if (value in attributes_present) and (not consistent) and (len(dependent)==len(attributes_present)):
                    prob = 1/len(attributes_present)
                elif (value in attributes_present) and (not consistent):
                    prob = 0.8/len(attributes_present)
                elif (value in attributes_present) and (consistent):
                    prob = 1
                elif (value not in attributes_present) and (consistent):
                    prob = 0
                else:
                    prob = 0.2/((len(dependent))-len(attributes_present))
                assignment = {'value': f'{value}', 'prob': prob}
                rv_assignment[f'{letter}{i+1}={key}'] = assignment
        rv_assignments[determinant] = rv_assignment
    return rv_assignments
