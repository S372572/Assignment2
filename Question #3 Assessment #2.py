def encrypt(text, key):
    # Initialize an empty string to store the encrypted text
    encrypted_text = ""
    
    # Iterate over each character in the input text
    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Shift the character by the key value
            shifted = ord(char) + key
            
            # Handle lowercase letters
            if char.islower():
                # Wrap around if the shifted character goes past 'z'
                if shifted > ord('z'):
                    shifted -= 26
                # Wrap around if the shifted character goes before 'a'
                elif shifted < ord('a'):
                    shifted += 26
            
            # Handle uppercase letters
            elif char.isupper():
                # Wrap around if the shifted character goes past 'Z'
                if shifted > ord('Z'):
                    shifted -= 26
                # Wrap around if the shifted character goes before 'A'
                elif shifted < ord('A'):
                    shifted += 26
            
            # Append the shifted character to the encrypted text
            encrypted_text += chr(shifted)
        else:
            # If the character is not an alphabet letter, add it as is
            encrypted_text += char
    
    # Return the final encrypted text
    return encrypted_text

def decrypt(text, key):
    # Initialize an empty string to store the decrypted text
    decrypted_text = ""
    
    # Iterate over each character in the input text
    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Shift the character back by the key value
            shifted = ord(char) - key
            
            # Handle lowercase letters
            if char.islower():
                # Wrap around if the shifted character goes before 'a'
                if shifted < ord('a'):
                    shifted += 26
                # Wrap around if the shifted character goes past 'z'
                elif shifted > ord('z'):
                    shifted -= 26
            
            # Handle uppercase letters
            elif char.isupper():
                # Wrap around if the shifted character goes before 'A'
                if shifted < ord('A'):
                    shifted += 26
                # Wrap around if the shifted character goes past 'Z'
                elif shifted > ord('Z'):
                    shifted -= 26
            
            # Append the shifted character to the decrypted text
            decrypted_text += chr(shifted)
        else:
            # If the character is not an alphabet letter, add it as is
            decrypted_text += char
    
    # Return the final decrypted text
    return decrypted_text

# Original text to be encrypted
original_text = "Hello, World!"
# Key for the Caesar cipher
key = 3

# Encrypt the original text
encrypted_text = encrypt(original_text, key)
# Print the encrypted text
print(f"Encrypted: {encrypted_text}")

# Decrypt the encrypted text
decrypted_text = decrypt(encrypted_text, key)
# Print the decrypted text
print(f"Decrypted: {decrypted_text}")
