import snowflake.connector
from sqlalchemy import create_engine, text
from sqlalchemy.engine.url import URL
import os

# Enable logging
# import logging
# logging.basicConfig(level=logging.DEBUG)

# Define your connection parameters
account = 'chb08794.us-east-1'
user = 'SAICHAITANYA.E@PDITECHNOLOGIES.COM'
role = 'TEST_SOFTWARE_ENGINEER_FR'
warehouse = 'TEST_ADHOC_WH'
database = 'US_ZIP_CODE_METADATA__POPULATIONS_GEO_CENTROID_LATLNG_CITY_NAMES_STATE_DMA_DEMOGRAPHICS'
schema = 'ZIP_DEMOGRAPHICS'
authenticator = 'externalbrowser'  # Use externalbrowser for Okta SSO

try:
    print("Connecting with Snowflake connector...")
    # Establish the connection using Snowflake connector
    conn = snowflake.connector.connect(
        user=user,
        account=account,
        authenticator=authenticator,
        role=role,
        warehouse=warehouse,
        database=database,
        schema=schema
    )
    print("Connection established with Snowflake connector.")

    # Create a cursor object to interact with Snowflake
    cursor = conn.cursor()

    # Execute a simple query to verify connection
    print("Executing query with Snowflake connector...")
    cursor.execute("SELECT CURRENT_VERSION()")
    version = cursor.fetchone()
    print(f"Snowflake version: {version[0]}")

    cursor.execute("SELECT count(*) from ZIP_CODE_METADATA")
    version = cursor.fetchone()
    print(f"Zip code metadata count: {version[0]}")

    print(f"Executing query to select the first 100 rows from ZIP_CODE_METADATA with Snowflake connector...")
    cursor.execute(f"SELECT * FROM ZIP_CODE_METADATA LIMIT 100")

    # Fetch all the results
    rows = cursor.fetchall()
    print(f"Rows fetched from ZIP_CODE_METADATA:")
    for row in rows:
        print(row)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    cursor.close()
    conn.close()
