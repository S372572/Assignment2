# We have created a function as per the requirements of the question to take in an argument "s".
def convert_substring_into_ascii(s):
    # Firstly, we will initialize 2 variables where we will be saving the the substrings of letters and numbers.
    num_sub_string = ''
    letter_sub_string = ''

    # Secondly, we we will perform a couple of checks. We first check if the provided value is a string or not using the type function, if not, 
    # we exit the function. Then we check if the characters in the string are less than 16, we can do this through calling the len 
    # function on our argument and will return false in the case as required by the Q. 
    if type(s) != str:
        print(f"The provided value is not a string")
        return 0
    if len(s) < 16:
        print(f"The provided string is less than 16 characters")
        return 0
    
    # Thirdly, we will have to separate the string into numbers and letters which we will be doing by calling each character
    # from the string one-by-one through for-loop and then, through conditional statements, check if it is a number or alphabet.
    # We can check both of these things using pythons in-built functions of isdigit and isalpha. Then we will concatenate those characters
    # in the sub string variables which we had declared earlier.
    for char in s:
        if char.isdigit():
            num_sub_string += char
        elif char.isalpha():
            letter_sub_string += char
    
    # We, then print the respective substrings on the console for visibility.
    print(f"Number string: {num_sub_string}")
    print(f"Letter string: {letter_sub_string}")
    
    # Fourthly, we need to convert even numbers in the number string to ASCII decimal values. For this, we will first attempt to
    # filter out even numbers only and save them in an array. While researching, we found a simpler technique to run the for-loop 
    # in the case of arrays. The loop runs on our numbers substring similar as before and checks if the number is even using the modulus operation.  
    # In case if it is, it makes an array of even_numbers and adds them into it. Then we need to convert those even numbers 
    # into ascii characters. We again use for-loop, this time on our even_numbers array and using ord function, we find the 
    # ascii codes of each of those numbers and then save it in our even_numbers_ascii array.
    even_numbers = [char for char in num_sub_string if int(char) % 2 == 0]
    even_numbers_ascii = [ord(char) for char in even_numbers]
    
    # We, then print the respective even numbers and even number ascii codes on the console for visibility.
    print(f"Even numbers: {even_numbers}")
    print(f"ASCII codes of even numbers: {even_numbers_ascii}")
    
    # Finakky, we perform the same steps as mentioned in fourth to make an array for capital characters through checking if they are uppercase using
    # isupper function. Once we have the array of the uppercase characters, we attempt to convert them into ascii codes using
    # previously mentioned strategy.
    upper_letters = [char for char in letter_sub_string if char.isupper()]
    upper_letters_ascii = [ord(char) for char in upper_letters]
    
    # We, then print the respective alpha uppercase character and their ascii codes on the console for visibility.
    print(f"Upper-case letters: {upper_letters}")
    print(f"ASCII codes of upper-case letters: {upper_letters_ascii}")

# We will attempt to call our function using the string mentioned in the question. For this, we simply assign the string value
# to a variable "s" and then pass it as an argument to the function we made.
s = '56aAww1984sktr235270aYmn145ss785fsq31D0'
s = 7
convert_substring_into_ascii(s)
