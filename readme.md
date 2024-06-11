# Generating requirements.txt
pip freeze > requirements.txt

# Setup Instructions
## Step-1: Create Virtual Environment
python -m venv venv
./venv/Scripts/activate

## Step-2: Install dependencies
pip install -r requirements.txt

# Handling Encryption of credentials - Do this before git push
1. Update config/SnowflakeConfig.json with actual credentials as key-value pairs
    Make use of variables file in Project directory for examples
2. Update SnowflakeConfigKeysToEncrypt.txt with all the keys that are to be encrypted in SnowflakeConfig file
3. Navigate to cryptoUtils/EncryptDecryptConfig.py and run the program - This encrypts SnowflakeConfig.json 
    Only the keys listed in SnowflakeConfigKeysToEncrypt file will be encrypted. The rest are left as they are.

# Update tests
