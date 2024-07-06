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
        return rows
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

def fetch_inconsistent_records(table_name,main_attributes,dependent_attributes):
    main_query_select = ", ".join([f"t1.{attr}" for attr in main_attributes + dependent_attributes])
    fd_condition_to_be_appended = " OR ".join([f"t1.{attr} <> t2.{attr}" for attr in dependent_attributes])
    return Queries.INCONSISTENT_RECORDS_QUERY.format(main_query_select=main_query_select,
                                         table_name=table_name,
                                         fd_condition_to_be_appended=fd_condition_to_be_appended)
    return final_sql

def fetch_consistent_records(table_name,main_attributes,dependent_attributes):
    main_query_select = ", ".join([f"t1.{attr}" for attr in main_attributes + dependent_attributes])
    fd_condition_to_be_appended = " OR ".join([f"t1.{attr} <> t2.{attr}" for attr in dependent_attributes])
    return Queries.CONSISTENT_RECORDS_QUERY.format(main_query_select=main_query_select,
                                                     table_name=table_name,
                                                     fd_condition_to_be_appended=fd_condition_to_be_appended)
    return final_sql
