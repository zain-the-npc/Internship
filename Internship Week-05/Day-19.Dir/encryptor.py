# encryptor.py

from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_message(message: str, password: str) -> str:
    key = generate_key(password)
    fernet = Fernet(key)
    token = fernet.encrypt(message.encode())
    encoded = base64.urlsafe_b64encode(token).decode()
    return encoded 

def decrypt_message(code: str, password: str) -> str:
    key = generate_key(password)
    fernet = Fernet(key)
    # Pad base64 to length divisible by 4
    padded_code = code + '=' * ((4 - len(code) % 4) % 4)
    try:
        token = base64.urlsafe_b64decode(padded_code)
        return fernet.decrypt(token).decode()
    except Exception:
        return "[Invalid code or password]"
