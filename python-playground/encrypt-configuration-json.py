import sys
import os


# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cryptoUtils.EncryptDecrypt import EncryptDecrypt
import json

# Read the key from the keys.txt file
keys_file = "./config/json-keys-to-be-encrypted.txt"
with open(keys_file, 'r') as file:
    keys = [line.strip() for line in file.readlines()]

config_file = "./config/configuration.json"
with open(config_file, 'r') as file:
    config_data = json.load(file)

encrypt_decrypt_instance = EncryptDecrypt()
# Encrypt each key listed in keys.txt and update the configuration.json file
for key in keys:
    if key in config_data:
        encrypted_value = encrypt_decrypt_instance.encrypt(config_data[key])
        config_data[key] = encrypted_value

# Write the updated configuration.json file
with open(config_file, 'w') as file:
    json.dump(config_data, file, indent=4)

print("Encryption complete. Configuration file updated.")