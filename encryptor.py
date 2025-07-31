import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend


def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a Fernet key from the given password and salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def encrypt_file(file_path, password):
    """Encrypt the file with the given password."""
    if not os.path.isfile(file_path):
        print("❌ File not found.")
        return

    salt = os.urandom(16)
    key = derive_key(password, salt)
    fernet = Fernet(key)

    with open(file_path, 'rb') as f:
        data = f.read()

    encrypted_data = fernet.encrypt(data)
    encrypted_file = file_path + ".encrypted"

    with open(encrypted_file, 'wb') as f:
        f.write(salt + encrypted_data)

    os.remove(file_path)  # Delete original

    print(f"✅ File encrypted and saved as: {encrypted_file}")
    print(f"🗑️ Original file '{file_path}' has been deleted.")


def decrypt_file(file_path, password):
    """Decrypt the file with the given password."""
    if not os.path.isfile(file_path):
        print("❌ File not found.")
        return

    with open(file_path, 'rb') as f:
        content = f.read()

    salt = content[:16]
    encrypted_data = content[16:]

    key = derive_key(password, salt)
    fernet = Fernet(key)

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        print("❌ Decryption failed. Incorrect password or corrupted file.")
        return

    # Restore original filename
    if file_path.endswith(".encrypted"):
        original_file = file_path.replace(".encrypted", "")
    else:
        original_file = file_path + ".decrypted"

    with open(original_file, 'wb') as f:
        f.write(decrypted_data)

    os.remove(file_path)  # Delete encrypted file

    print(f"✅ File decrypted and restored as: {original_file}")
    print(f"🗑️ Encrypted file '{file_path}' has been deleted.")


def main():
    print("🔐 Secure File Encryption System")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Enter your choice (1/2): ").strip()

    file_path = input("Enter full path of the file: ").strip()
    password = input("Enter password: ").strip()

    if choice == "1":
        encrypt_file(file_path, password)
    elif choice == "2":
        decrypt_file(file_path, password)
    else:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
