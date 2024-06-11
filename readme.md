# Generating requirements.txt - To be used only when new dependencies are added
pip freeze > requirements.txt

# Setup Instructions
## VS Code Editor
ctrl + shift + p == Python: Create Terminal

## Step-1: Create Virtual Environment
Run the command: python -m venv venv
Relaunch Python Terminal
Run the command: ./venv/Scripts/activate

## Step-2: Install dependencies
pip install -r requirements.txt

# Handling Encryption of credentials - Do this before git push
1. Update config/SnowflakeConfig.json with actual credentials as key-value pairs
    Make use of variables file in Project directory for examples
2. Update(if required) SnowflakeConfigKeysToEncrypt.txt with all the keys that are to be encrypted in SnowflakeConfig file
3. Navigate to cryptoUtils/EncryptDecryptConfig.py and run the program - This encrypts SnowflakeConfig.json 
    Only the keys listed in SnowflakeConfigKeysToEncrypt file will be encrypted. The rest are left as they are.

# Update tests
 At runtime the fixture in conftest will decrypt the encrypted snowflakeconfig values and establish a connection
 Feel free to edit utils/SnowflakeUtils.py as per your requirement
    example - modify implementation for method: def fetch_rows(self, table_name, limit=100)