# -*- coding: utf-8 -*-

#question 3 part 2
def decrypt(text, key):
    decrypted_text = ''
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) - key  # Shift character back by key
            if char.islower():  # Handle lowercase characters
                if shifted < ord('a'):  # Wrap around if below 'a'
                    shifted += 26
            elif char.isupper():  # Handle uppercase characters
                if shifted < ord('A'):  # Wrap around if below 'A'
                    shifted += 26
            decrypted_text += chr(shifted)  # Convert back to character
        else:
            decrypted_text += char  # Keep non-alphabet characters unchanged
    return decrypted_text

# Example usage
encrypted_text = "l'sgd `fnk enq sgd hmbsqxosdc bncdc"
key = 1  # Key to decrypt (replace with correct key)
decrypted_text = decrypt(encrypted_text, key)
print(decrypted_text)

#question 3 part 3
total = 0  # Correct variable initialization
for i in range(5):  # Range should start from 0 to 4
    for j in range(5):  # Correct inner loop range
        if j % 2 == 0:  # Correct condition to check even index
            total += i + j  # Add both i and j to total
        else:
            total -= i - j  # Subtract i - j from total

print(total)  # Print the correct total value

# The corrected nested loop logic is fixed to properly sum and subtract values

#question 3 part 4
# Decryption function
def decrypt(text, key):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Encrypted code to decrypt
encrypted_text = "l'sgd `fnk enq sgd hmbsqxosdc bncdc"
key = 1  # Adjust based on actual decryption key
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted Code:", decrypted_text)

# Corrected code
total = 0
for i in range(5):
    for j in range(5):
        if j % 2 == 0:
            total += i + j
        else:
            total -= i - j

print(total)