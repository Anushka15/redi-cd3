# database/fetch_data.py

from database.connection import create_connection
from constants.queries import Queries

def fetch_data_results(query):
    conn = create_connection()
    if not conn:
        return None
    try:
        result = conn.execute(query)
        rows = result.fetchall()
        if conn:
            conn.close()
        return rows
    except Exception as e:
        print(f"Error executing query: {e}")
        if conn:
            conn.close()
        return None

def find_inconsistent_records(table_name,determinant_attributes,dependent_attributes):
    main_query_select = ", ".join([f"t1.{attr}" for attr in determinant_attributes + dependent_attributes])
    fd_condition_to_be_appended = " OR ".join([f"t1.{attr} <> t2.{attr}" for attr in dependent_attributes])
    return Queries.INCONSISTENT_RECORDS_QUERY.format(main_query_select=main_query_select,
                                         table_name=table_name,
                                         fd_condition_to_be_appended=fd_condition_to_be_appended)
    return final_sql

def find_consistent_records(table_name,determinant_attributes,dependent_attributes):
    main_query_select = ", ".join([f"t1.{attr}" for attr in determinant_attributes + dependent_attributes])
    fd_condition_to_be_appended = " OR ".join([f"t1.{attr} <> t2.{attr}" for attr in dependent_attributes])
    return Queries.CONSISTENT_RECORDS_QUERY.format(main_query_select=main_query_select,
                                                     table_name=table_name,
                                                     fd_condition_to_be_appended=fd_condition_to_be_appended)
    return final_sql

def find_distinct_attribute_values(table_name,attribute_name):
    return Queries.SELECT_DISTINCT_ATTRIBUTE_VALUES.format(attribute_name=attribute_name,
                                                           table_name=table_name)

def find_where_determinant(table_name,determinant_attribute,dependent_attributes,determinant_value):
    main_query_select = ", ".join([f"t1.{attr}" for attr in dependent_attributes])
    return Queries.FIND_WHERE_DETERMINANT.format(main_query_select=main_query_select,
                                                           table_name=table_name,
                                                 determinant_attribute=determinant_attribute,
                                                 determinant_value=determinant_value)

def fetch_all_records(table_name,determinant_attributes,dependent_attributes):
    main_query_select = ", ".join([f"t1.{attr}" for attr in determinant_attributes+dependent_attributes])
    return Queries.FETCH_ALL_DATA.format(main_query_select=main_query_select,
                                                           table_name=table_name)
