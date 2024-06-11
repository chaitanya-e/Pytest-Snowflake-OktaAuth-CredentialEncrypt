import sys
import os
import json
import base64


# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cryptoUtils.EncryptDecrypt import EncryptDecrypt

# Read the key from the keys.txt file
keys_file = "./config/json-keys-to-be-encrypted.txt"
with open(keys_file, 'r') as file:
    keys = [line.strip() for line in file.readlines()]

# Read the configuration.json file
config_file = "./config/configuration.json"
with open(config_file, 'r') as file:
    config_data = json.load(file)

# Create an instance of the EncryptDecrypt class with the decoded key
encrypt_decrypt_instance = EncryptDecrypt()

# Dictionary to store decrypted values
decrypted_values = {}

# Decrypt each key listed in keys.txt and store in separate variables
for key in config_data:
    if key in keys:
        encrypted_value = config_data[key]
        decrypted_value = encrypt_decrypt_instance.decrypt(encrypted_value)
        decrypted_values[key] = decrypted_value
    else:
        decrypted_values[key] = config_data[key]
    
# Print the decrypted values
for key, value in decrypted_values.items():
    print(f"{key} = {value}")
