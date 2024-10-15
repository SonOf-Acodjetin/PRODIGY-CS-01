# Function to encrypt the text using Caesar Cipher
def encrypt(text, shift):
    result = ""
    # Loop through each character in the text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabetic characters unchanged
        else:
            result += char
    return result

# Function to decrypt the text using Caesar Cipher
def decrypt(text, shift):
    result = ""
    # Loop through each character in the text
    for char in text:
        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        # Leave non-alphabetic characters unchanged
        else:
            result += char
    return result

# Main program
def main():
    print("Caesar Cipher Encryption & Decryption")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'encrypt':
        print("Encrypted message: ", encrypt(message, shift))
    elif choice == 'decrypt':
        print("Decrypted message: ", decrypt(message, shift))
    else:
        print("Invalid option. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
