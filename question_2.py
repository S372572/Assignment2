# -*- coding: utf-8 -*-

#question no 2 chapter 1
from PIL import Image

# Load the image
image = Image.open('chapter1.jpg')
pixels = image.load()

n = 5  # Example value for 'n', replace with actual algorithm output

# Modify the pixels
for i in range(image.size[0]):
    for j in range(image.size[1]):
        r, g, b = pixels[i, j]
        pixels[i, j] = (r + n, g + n, b + n)

# Save the modified image
image.save('chapter1out.png')

# Sum all red pixel values in the new image
red_sum = sum(pixels[i, j][0] for i in range(image.size[0]) for j in range(image.size[1]))
print(f"Sum of Red Pixels: {red_sum}")

#question no 2 chapter 2
def decrypt_code(encrypted_code, key):
    # Decryption logic based on the pattern
    decrypted_code = ''.join([chr(ord(char) - key) for char in encrypted_code])
    return decrypted_code

# Example encrypted code and key
encrypted_code = "..."
key = 5  # Replace with actual key

decrypted_code = decrypt_code(encrypted_code, key)
print(f"Decrypted Code: {decrypted_code}")