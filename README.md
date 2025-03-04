# Secure File Encryption Tool

A beginner-friendly Python tool for encrypting and decrypting files using AES via the `cryptography` library's Fernet module, designed to teach secure coding practices.

## Features
- Encrypts files with a unique key using AES encryption.
- Decrypts files with the correct key.
- Includes robust error handling for invalid inputs, keys, or files.
- Warns users about redundant encryption attempts.
- User-friendly command-line interface.

## Technologies
- **Language**: Python (3.8+ recommended)
- **Library**: `cryptography` (for Fernet/AES implementation)
- **Tools**: Visual Studio Code, macOS Terminal
- **Operating System**: Developed and tested on macOS

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


## Example Output
### Encryption
Would you like to (e)ncrypt or (d)ecrypt a file? (e/d): e

Enter the file name: test.txt

Save this key securely: gAAAAABk... (example key, save this!)

File encrypted as test.txt.encrypted

### Decryption
Would you like to (e)ncrypt or (d)ecrypt a file? (e/d): d

Enter the file name: test.txt.encrypted

Enter the key: gAAAAABk... (paste saved key)

File decrypted as test_decrypted.txt
