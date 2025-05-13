# Demonstrate how variables are created and how they work
# Author: Caleb Prestidge
# Date: 11/4/2025

# Different types of variables
# Store a number
my_number = 80 # assinging 80 to my_number (variable)
print(my_number)

my_number2 = 7 # I have reassigned the value of the variable
print(my_number2)

# Store a string
name_1 = "Caleb"
print(name_1)
# assign the value of one variable to another
my_number = name_1
print(my_number)  # don't assign values to variables that don't make sense

# creating a new variable
num_1 = 5
num_2 = 17

''' Do calculations with variables and store the result in
 another variable. I can now 
 press enter
 as
 many times
 as I want'''

sum = 5+17 # This is not good practice
print(sum)

# Better way
sum1 = num_1 + num_2
print(sum1)

sum_string = "17" # This stores a string
sum_string2 = "5"

# adding strings together is called concatenation.
sum = sum_string + sum_string2
print(sum)
print(sum1)

print(f"My calculation for {sum_string} + {sum_string2} = {sum1}")