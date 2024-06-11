def test_fetch_rows_from_snowflake(establish_snowflake_connection):
    table_name = "ZIP_CODE_METADATA";

    # Fetch rows from the specified table
    rows = establish_snowflake_connection.fetch_rows(table_name, limit=100)
    
    # Check that rows are returned
    print("Number of rows returned = "+str(len(rows)))
    assert rows is not None, "No rows were returned"
    assert len(rows) <= 100, "More than 100 rows were returned"
    