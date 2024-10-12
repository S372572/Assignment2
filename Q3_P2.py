# Q3
# These are the predefined values of a global variable and a dictionary which we will be editing through the code below.
global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# This is a function that runs on a list of values and removes certain number of values. 
# Originally the function didn't have any argument therefore it was giving an error. Now, when we have defined the function
# using an argument named "argument1", it would run smoothly.
# def process_numbers():
def process_numbers(argument1):
    global global_variable     
    local_variable = 5
    numbers = [1, 2, 3, 4, 5] # A numbers array is declared here which will be used in the while-loop below.
    numbers = argument1 # If we wish to use our own list of values then we will have to over-write the previous list with our
                        # own. Therefore, we will have to point the numbers variable to our own, called through argument1. 

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable) # This code will run a while-loop to remove the values from the 
                                            # provided list which are less than 5, greater than 0, and divisible by 2.
        local_variable -= 1
    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
#  result = process_numbers(numbers=my_set)
#corrected
result = process_numbers(my_set) # Here we have called the function with a set named "my_set". The initial provided syntax was
                                # wrong, if we want to set / change the value of the numbers variable, we will do it through
                                # the procedure mentioned above.

# def modify_dict():
def modify_dict(local_variable): # The error here was similar, there was no argument declared.
    local_variable = 10 # The local_variable is mentioned here with the value 10, it will over-write the value of our are argument.
    my_dict['key4'] = local_variable # If we want to use our own argument's value here, then we'll have to remove the explicit 
                                    # declaration of "local_variable = 10" above.

modify_dict(5) # Here we are calling the modify_dict function with the value 5 as argument.

def update_global():
   global global_variable # This function will be updating the value of our globally declared variable named global_variable, 
   global_variable += 10 # and add 10 into it when called.

#corrected
update_global() # There was a logical error here as the update_global function was never called, therefore we have called it here.

for i in range(5): # This loop is running needlessly as it doesn't have any impact on our code.
    print(i)
    i += 1

if my_set is not None and my_dict['key4'] == 10: # This conditional statement checks if my_set isn't None and the value of
    print("Condition met!") # "key4" is 10 in my_dict, it will print "Condition met!" on the terminal.

if 5 not in my_dict: # This condition will check whether a key named "5" is in my_dict. 
    print("5 not found in the dictionary!")

print (global_variable)
print(my_dict)
print(my_set)
