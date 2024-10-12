# The provided cipher is made using substitution mechanism, which is a simple encryption logic. To decrypt the text, we 
# will create a decrypt function. The function will take in 2 arguments, first argument "ciphervalue" will need to be passed 
# the cipher value and the second one "shift" will need to be passed the key value for shift.
def decrypt_substitution_cipher(ciphervalue, shift):
    decrypted_value = "" # We will declare a string variable to concatenate the results into.
    
    # We will attempt to run a for-loop on the cipher text that would be provided in the argument. The loop will separately 
    # call each character in the cipher text string.
    for character in ciphervalue:
        if character.isalpha():  # We will first check if the character is alphabetic, for which we can use isalpha function.
            ascii_offset = 65 if character.isupper() else 97 # This shortened (albeit a room for improvement) condtional statement 
                                                        # checks if the character is lowercase or upper in case of the character "A"
            decrypted_character = chr((ord(character) - ascii_offset - shift) % 26 + ascii_offset) # We then make sort of a formula to  
            # calculate and convert the ascii value to character. For this we first use ord() function on our character to find
            # the ascii code of the character, we then subtract the offset and the shift value to perform the modulus function using
            # 26 (as there are 26 aplhabets). We will re-add the ascii offset value to be retrieve the code of the character that would
            # be changed using the shift, and finally, using the chr() function, we can convert the value to character.
            decrypted_value += decrypted_character # We concatenate the decrypted character in our decrypted_value string.
        else:
            decrypted_value += character  # If there are any non-alphabetic characters, they will be concatenated as it is in the string.

    return decrypted_value # We will retrun the result after the process is completed.

# We will then creat a function to try all possible shifts. Note, we can do this through a loop as well but for ease of understanding
# we have made a function. The argument for the function will be the cipher text that is provided to us.
def shift_key_tries(ciphervalue):
    for shift in range(1, 26): # We simply start the loop for characters 1 to 26 and then call the decrypt_substitution_cipher
        # function with the ciphervalue in the question and attempt to try it with shift values.
        print(f"Shift {shift}: {decrypt_substitution_cipher(ciphervalue, shift)}\n") 

# We have saved the cipher quote in question in a variable as a string.
ciphered_quote = "VZ FRYSFU VZCNGVRAG NAQ N YVGGYR VARPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEG GURA LBH FHER NF URYYOBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

shift_key_tries(ciphered_quote) # Finally, we call the shift_key_tries function on the quote.

#ANSWER: Shift 13: IM SELFSH IMPATIENT AND A LITTLE INECURE I MAKE MISTAKES I AM OUT OF CONTROL ANDAT TIMES HARD TO HANDLE BUT IF YOU CANT HANDLE ME AT MY WORT THEN YOU SURE AS HELLBONT DESERVE ME AT MY BEST MARILYN MONROE