import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Load the AES key from an environment variable
BASE64_KEY = "ZPuXewhlZ3PIsCfIhDdE/D8X65OT/ngRHtheoPHDCZE="
KEY = base64.b64decode(BASE64_KEY)

class EncryptDecrypt:
        
    def encrypt(self, plain_text):
        cipher = AES.new(KEY, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return {'iv': iv, 'ciphertext': ct}

    def decrypt(self, enc_dict):
        iv = base64.b64decode(enc_dict['iv'])
        ct = base64.b64decode(enc_dict['ciphertext'])
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8')
