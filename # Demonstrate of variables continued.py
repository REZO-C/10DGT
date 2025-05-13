# Demonstrate of variables continued
# Author Danny Kim
# Date 7 May 2025
# Version 1

# Ask the user a question and store their answer in a variable
# Ask the user for their name and store it
name = input("Kia ora, what is your name? ")
print() # this is a line break

print(f"Nice to meet you, {name}")
print()

# Ask the user for two numbers and then add them together.
num1 = int(input("What is your first number please? "))
print()
num2 = int(input('What is your second number? '))
print()
print(f"You entered your first number as {num1}")
print()
print(f"You entered your second number as {num2}")

# Adding the two answers together
sum = num1 + num2
print(sum)

# Muliplying the 2 numbers
multipy = num1 * num2
print(f"The two number multiplied will result in {multipy}")

# Test that input was stored correctly
print(name)
# To comment code out, use ctrl + /