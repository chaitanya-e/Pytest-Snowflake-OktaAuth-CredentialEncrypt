import json
import os
from cryptoUtils.EncryptDecrypt import EncryptDecrypt

class ConfigManager:
    def __init__(self, keys_file_path, config_file_path):
        self.keys_file_path = keys_file_path
        self.config_file_path = config_file_path
        self.encrypt_decrypt_instance = EncryptDecrypt()
        self.keys = self._read_keys()

    def _read_keys(self):
        """Read keys from the keys file."""
        try:
            with open(self.keys_file_path, 'r') as file:
                keys = [line.strip() for line in file.readlines()]
            return keys
        except Exception as e:
            raise Exception(f"Failed to read keys file: {e}")

    def _read_config(self):
        """Read the configuration file."""
        try:
            with open(self.config_file_path, 'r') as file:
                config_data = json.load(file)
            return config_data
        except Exception as e:
            raise Exception(f"Failed to read configuration file: {e}")

    def _write_config(self, config_data):
        """Write the configuration file."""
        try:
            with open(self.config_file_path, 'w') as file:
                json.dump(config_data, file, indent=4)
        except Exception as e:
            raise Exception(f"Failed to write configuration file: {e}")

    def encrypt_config(self):
        """Encrypt the values in the configuration file."""
        config_data = self._read_config()
        for key in self.keys:
            if key in config_data:
                encrypted_value = self.encrypt_decrypt_instance.encrypt(config_data[key])
                config_data[key] = encrypted_value
        self._write_config(config_data)
        print("Encryption complete. Configuration file updated.")

    def decrypt_config(self):
        """Decrypt the values in the configuration file and return them."""
        config_data = self._read_config()
        decrypted_values = {}

        for key in config_data:
            if key in self.keys:
                try:
                    decrypted_value = self.encrypt_decrypt_instance.decrypt(config_data[key])
                    decrypted_values[key] = decrypted_value
                except Exception as e:
                    print(f"Error decrypting {key}: {e}")
                    decrypted_values[key] = config_data[key]
            else:
                decrypted_values[key] = config_data[key]

        return decrypted_values


# To be run in order to encrypt credentials
if __name__ == "__main__":
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

    # Encrypt the configuration file
    manager.encrypt_config()
