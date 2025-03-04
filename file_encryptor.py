from cryptography.fernet import Fernet, InvalidToken  # Import InvalidToken explicitly

def encrypt_file(file_name, key):
    cipher = Fernet(key)
    with open(file_name, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    output_file = file_name + '.encrypted'
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)
    print(f"File encrypted as {output_file}")

def decrypt_file(file_name, key):
    cipher = Fernet(key)
    try:
        with open(file_name, 'rb') as file:
            encrypted_data = file.read()
        # Attempt to verify the token before full decryption
        cipher._get_unverified_token_data(encrypted_data)  # Check if it's a valid token
        decrypted_data = cipher.decrypt(encrypted_data)
        output_file = file_name.replace('.encrypted', '_decrypted.txt')
        with open(output_file, 'wb') as file:
            file.write(decrypted_data)
        print(f"File decrypted as {output_file}")
    except InvalidToken:
        print(f"Error: '{file_name}' is not a valid encrypted file or the key is incorrect. Use a .encrypted file.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Unexpected error during decryption: {e}")

if __name__ == "__main__":
    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt a file? (e/d): ").lower()
        if choice in ['e', 'd']:
            break
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

    file_name = input("Enter the file name: ").strip()

    if choice == 'e':
        if file_name.endswith('.encrypted'):
            print("Warning: This file looks encrypted already. Are you sure?")
            if input("Continue? (y/n): ").lower() != 'y':
                print("Operation canceled.")
                exit()
        try:
            key = Fernet.generate_key()
            print("Save this key securely:", key.decode())
            encrypt_file(file_name, key)
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except Exception as e:
            print(f"Unexpected error during encryption: {e}")
    elif choice == 'd':
        try:
            with open(file_name, 'rb') as file:
                encrypted_data = file.read()
            # Pre-check the file to ensure it's a valid token
            Fernet._get_unverified_token_data(encrypted_data)  # Use Fernet class directly
            key = input("Enter the key: ").encode()
            decrypt_file(file_name, key)
        except InvalidToken:
            print(f"Error: '{file_name}' is not a valid encrypted file. Please use a .encrypted file.")
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except Exception as e:
            print(f"Unexpected error: {e}")
