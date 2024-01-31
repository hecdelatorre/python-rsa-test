from keychain_operations import generate_keys
from encryption_operations import encrypt_message, decrypt_message

# Variable to store encrypted text
encrypted_text = ""

def print_menu():
    print("Menu:")
    print("1. Generate Keys")
    print("2. Encrypt Message")
    print("3. Decrypt Message")
    print("e. Exit")

def main():
    global encrypted_text
    while True:
        print_menu()
        option = input("Select an option: ")

        if option.isdigit():
            option = int(option)
            if option == 1:
                generate_keys()
            elif option == 2:
                message = input("Enter the message to encrypt: ")
                encrypted_text = encrypt_message(message)
                print("Message encrypted successfully.")
            elif option == 3:
                if encrypted_text:
                    decrypted_text = decrypt_message(encrypted_text)
                    print("Decrypted message:", decrypted_text)
                else:
                    print("No encrypted text available. Please encrypt a message first.")
            else:
                print("Invalid option. Please try again.")
        elif option.lower() == 'e':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter a valid option.")

if __name__ == "__main__":
    main()
