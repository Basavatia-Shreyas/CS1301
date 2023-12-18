#Recall that input from a user is always in the form of a string. 
#Write a function called "input_type" that gets user input and 
#determines what kind of string the user entered. The user input
#will be supplied as an argument to the function like normal.
#
#  - Your function should return "integer" if the string only
#    contains characters 0-9.
#  - Your function should return "float" if the string only
#    contains the numbers 0-9 and at most one period.
#  - You should return "boolean" if the user enters "True" or
#    "False". 
#  - Otherwise, you should return "string".


#Write your function here!
def input_type(user_input):
    if(user_input == ""):
        return "string"
    if(user_input == "False" or user_input == "True"):
        return "boolean"
    period = 0
    nums = True
    for i in user_input:
        if i == ".":
            period += 1
        if i not in "1234567890.":
            nums = False
    if nums and period == 0:
        return "integer"
    elif nums and period == 1:
        return "float"
    else:
        return "string"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#string
#boolean
#float
#integer
print(input_type(""))
print(input_type("False"))
print(input_type("7.432621"))
print(input_type("2788"))




