# 🔐 Secure File Encryption System

A simple Python-based tool to encrypt and decrypt files using AES encryption and password-based key derivation. Ensures secure file storage and transfer.

---

## 📌 Features

- 🔐 Encrypt any file with a password
- 🔓 Decrypt file using the same password
- 📦 AES-256 encryption with secure salt and PBKDF2 key derivation
- 🗑️ Automatically deletes original/encrypted file
- ✅ Easy command-line interface (CLI)

---

## 🛠️ Technologies Used

- Python 3
- `cryptography` library

---

## 📁 Project Structure

Secure-File-Encryption/
├── encryptor.py # Main script
└── README.md # Documentation


---

## 🚀 How to Run

### ▶️ Step 1: Install Required Library
```bash
pip install cryptography

### ▶️ Step 2: Run the Program
python encryptor.py
Follow the on-screen instructions:

Choose 1 to encrypt or 2 to decrypt

Enter the full file path

Enter your password

📂 Output Files
Encrypted file: filename.extension.encrypted

Decrypted file: filename.extension (restored)
