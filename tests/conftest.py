import pytest
import json
import os
from utils.SnowflakeUtils import SnowflakeConnector
from cryptoUtils.EncryptDecryptConfig import ConfigManager

@pytest.fixture(scope='module')
def establish_snowflake_connection():
    # Determine the directory containing the conftest.py file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the path to the FilePaths.json file relative to the conftest.py file
    file_paths = os.path.join(current_dir, '../config/FilePaths.json')
    # Ensure the path is absolute and normalized
    file_paths = os.path.abspath(file_paths)
    
    with open(file_paths, 'r') as file:
        file_path = json.load(file)

    # Create an instance of ConfigManager
    keys_path = os.path.join(current_dir, file_path["SnowflakeConfigKeys"])
    config_path = os.path.join(current_dir, file_path["SnowflakeConfig"])
    manager = ConfigManager(keys_path, config_path)
    config = manager.decrypt_config()

    # Initialize the Snowflake connector
    connector = SnowflakeConnector(
        account=config['account'],
        user=config['user'],
        role=config['role'],
        warehouse=config['warehouse'],
        database=config['database'],
        schema=config['schema'],
        authenticator=config['authenticator']
    )

    # Connect to Snowflake
    connector.connect()

    yield connector

    # Close the connection
    connector.close()