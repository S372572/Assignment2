# Figuring out the key 
total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j 
        else:
            total -= i - j

counter = 0
while counter < 5:
    if total < 13:
        total += 1 
    elif total > 13:
        total -= 1 
    else:
        counter += 2

print(total) # The total variable contained the value of 13 which is our Key

# The logic to reverse the Encrypt function was pretty simple. The encryption model used, relied upon character substition. 
# All we had to do was to switch the signs where applicable to make the decrypt function.
def decrypt(encrypted_text, key): # First we will take 2 inputs through arguments, "encrypted text" and "key" value.
    decrypted_text = "" # We will initialize a variable to save our string value of the decrypted text.
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key # Here we will calculate the shifted value by subtracting the key from the ASCII value
            if char.islower(): # of the char. Note that it's the exact opposite case of the encrypt function where we were adding these vaules.
                if shifted < ord('a'):
                    shifted += 26 # From here on, based on the conditional statements which were mentioned in the encrypt function,
                elif shifted > ord('z'): # We use them as the premise and simply reverse the shifted value (Subtract where the shift was ahead, Add where the shift was backwards.)
                    shifted -= 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
            decrypted_text += chr(shifted)
        else: 
            decrypted_text += char 
    print (decrypted_text) # We will finally output the decypted value

# Using multi-line string, we will pass the function, encrypted code
a = """
tybony_inevnoyr = 100 
zl_qvpg = {‘xrll': 'inyhrl', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3’}  

qrs cebprff ahzoref () :  
    tybony tybony_inevnoyr  
    ybpny_inevnoyr = 5  
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0: 
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny inevnoyr -= 1  

    erghea ahzoref  

z1_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}  
erfhyg = cebprff_ahzoref(ahzoref=z1 frg)  

qrs zbqvsl_qvpg():  
    ybpny inevnoyr = 10  
    z1_qvpg['xr14'] = ybpny_inevnoyr  

zbqvs1_qupg(5)  

qrs hcqngr_tybony ():  
    tybony tybony inevnoyr  
    tybony inevnoyr += 10  

sbe v va enatr(5):  
    cevag(v)  
    V += 1  

vs z1_frg vf abg Abar naq z1_qvpg['xr14'] == 10:  
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur gvpgvbanel!")

cevag (tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""

decrypt(a, 13) # Here we call our decrypt function to decrypt our code using the key value of 13 which was found above.
