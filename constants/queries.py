class Queries:

    INCONSISTENT_RECORDS_QUERY = """
        SELECT {main_query_select}
        FROM {table_name} t1
        WHERE EXISTS (
            SELECT 1
            FROM {table_name} t2
            WHERE t1.person = t2.person
            AND ({fd_condition_to_be_appended})
        )
    """

    CONSISTENT_RECORDS_QUERY = """
            SELECT {main_query_select}
            FROM {table_name} t1
            WHERE NOT EXISTS (
                SELECT 1
                FROM {table_name} t2
                WHERE t1.person = t2.person
                AND ({fd_condition_to_be_appended})
            )
        """

    SELECT_DISTINCT_ATTRIBUTE_VALUES = """
            SELECT DISTINCT({attribute_name})
            FROM {table_name} t1
    """

    FIND_WHERE_DETERMINANT = """
            SELECT {main_query_select}
            FROM {table_name} t1
            WHERE {determinant_attribute} = '{determinant_value}'
    """

    FETCH_ALL_DATA = """
            SELECT {main_query_select}
            FROM {table_name} t1
    """