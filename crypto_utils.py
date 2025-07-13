# crypto_utils.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from hashlib import sha256
import os

def pad(data):
    return data + b' ' * (16 - len(data) % 16)

def get_key(password):
    return sha256(password.encode()).digest()

def encrypt_file(in_file, out_file, password):
    key = get_key(password)
    cipher = AES.new(key, AES.MODE_CBC)
    with open(in_file, 'rb') as f:
        data = pad(f.read())
    iv = cipher.iv
    encrypted = cipher.encrypt(data)
    with open(out_file, 'wb') as f:
        f.write(iv + encrypted)

def decrypt_file(in_file, out_file, password):
    key = get_key(password)
    with open(in_file, 'rb') as f:
        iv = f.read(16)
        encrypted = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    data = cipher.decrypt(encrypted).rstrip(b' ')
    with open(out_file, 'wb') as f:
        f.write(data)