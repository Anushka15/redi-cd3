import pandas as pd

#creating probabilistic database for the given inconsistent DB
#Assumption: Table structure is already created with columns: determinant attributes, dependent attributes, _sentence (BDD for dubio)
def create_probabilistic_db(sentences, determinant_attributes, dependent_attributes):
    column_names = [f'{determinant_attributes[0]}']
    for attribute in dependent_attributes:
        column_names.append(f'{attribute}')
    column_names.append('_sentence')
    # Initialize an empty DataFrame with the specified columns
    prob_data = pd.DataFrame(columns=column_names)

    # Iterate through the sentences
    for determinant, tuples_list in sentences.items():
        for tpl in tuples_list:
            entry = []
            dependents_tuple = tpl[0]
            sentence = tpl[1]
            entry.append(f'{determinant}')
            for dependent in dependents_tuple:
                entry.append(f'{dependent}')
            entry.append(f'{sentence}')
            prob_data.loc[len(prob_data)] = entry
    return prob_data