from Crypto.Random import get_random_bytes
import base64

# Generate a 32-byte key
key = get_random_bytes(32)
print("Your secure key (store it securely):", base64.b64encode(key).decode())

# Generated AES Key : ZPuXewhlZ3PIsCfIhDdE/D8X65OT/ngRHtheoPHDCZE=
