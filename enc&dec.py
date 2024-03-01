from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64

master_key = b'Vidg1ef3'  # Convert to bytes format by prefixing with 'b'
password = 'Vishat@'
part_pass = password[-1:3:-1]
print(part_pass)


def derive_key(master, partial_password):
    combined_key = master + partial_password.encode()  # Convert partial_password to bytes
    salt = partial_password.encode()
    # Derive a key using PBKDF2 with SHA-256
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 256 bits
        salt=salt,  # Salt can be added for additional security
        iterations=100000,  # Adjust as needed
        backend=default_backend()
    )
    derived_key = kdf.derive(combined_key)
    return derived_key


def encrypt_password(key, password_e):
    # Base64 encode the master key
    encoded_key = base64.urlsafe_b64encode(key)
    # Create a Fernet cipher with the encoded master key
    cipher = Fernet(encoded_key)
    # Encrypt the password
    encrypted_password = cipher.encrypt(password_e.encode())
    return encrypted_password


def decrypt_password(master, encrypted_password):
    # Create a Fernet cipher with the master key
    cipher = Fernet(base64.urlsafe_b64encode(master))
    # Decrypt the password
    decrypted_password = cipher.decrypt(encrypted_password).decode()
    return decrypted_password


derived_key = derive_key(master_key, password)
encrypted_password = encrypt_password(derived_key, password)
decrypted_password = decrypt_password(derived_key, encrypted_password)

print("Derived Key:", derived_key)
print("Encrypted Password:", encrypted_password)
print("Decrypted Password:", decrypted_password)
