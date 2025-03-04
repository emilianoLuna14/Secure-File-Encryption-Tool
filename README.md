# Secure File Encryption Tool

A Python-based utility for securely encrypting and decrypting files using the AES algorithm via the `cryptography` library's Fernet module.

## Features
- Encrypts files with a unique key using AES encryption.
- Decrypts files with the correct key.
- Includes robust error handling for invalid inputs, keys, or files.
- Warns users about redundant encryption attempts.
- User-friendly command-line interface.

## Technologies
- **Language**: Python
- **Library**: `cryptography`
- **Tools**: Visual Studio Code, macOS Terminal
- **OS**: Developed and tested on macOS

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/emilianoLuna14/Secure-File-Encryption-Tool.git

2. Navigate to the folder:
   run cd Secure-File-Encryption-Tool

3. Install the required library:
   pip3 install cryptography

## Usage
1. Run the script:
   python3 file_encryptor.py
   
2. Choose (e)ncrypt or (d)ecrypt.

3. Enter the file name (e.g., test.txt for encryption, test.txt.encrypted for decryption).

4. For encryption, save the generated key. For decryption, input the saved key.
