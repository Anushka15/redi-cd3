This project contains the Python implementation of the project: 'Constraint-Driven Data Doubting (CD3) Using Probabilistic Database Approach'.
To run the code, execute notebook: notebooks/rv_generation_prob_assignment.ipynb

Parameters like table_name, determinant_attributes and dependent_attributes can be changed dynamically dependin on the database used.

Example: for a funtional dependency: person -> {model,color}
determinant_attributes = ['person']
dependent_attributes = ['model','color']

Below functionalities are available (Function implementations in: probabilistic_database_creation/{rv_probability_assignments.py, prob_db_creation_dubio.py}
1) Generating RVs (generate_rvs(data,dependent_attributes))
2) Creating RV assignments and assigning probabilities: CWA - create_rv_assignments_with_prob_CWA(data,dependent_attributes_mappings,determinant_attributes,dependent_attributes)
3) Creating RV assignments and assigning probabilities: SWA - create_rv_assignments_with_prob_SWA(data,dependent_attributes_mappings,determinant_attributes,dependent_attributes)
4) Computing sentences: compute_sentences(rv_assignments_SWA,data,determinant_attributes)
5) Creating probabilistic database (Creates a dataframe which can be used for Dubio): create_probabilistic_db(sentences,determinant_attributes,dependent_attributes)
