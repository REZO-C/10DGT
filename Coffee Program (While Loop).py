# Demonstrate how to use while loops and if statements
# Caleb Prestidge
# 14 May
# Version 3

# While Loop
'''
keep_going = ""  # This variable contains an open string
while keep_going == "":

    like_coffee = input("Do you like Coffee?")

    if like_coffee == "yes":
        print("That's great. I like Coffee too!")
        keep_going = "finished"     
    ''''''

# Version 2
keep_going = ""
while keep_going == "":
    # .lower converts the answer to lower case
    like_coffee = input("Do you like Coffee?").lower()
    if like_coffee == "yes" or like_coffee == "y":
        print("That's great. I like Coffee too!")

    elif like_coffee =="no" or like_coffee =="n":
        print("You are missing out!") 

        like_tea = input("Do you like Tea instead?"). upper()

        if like_tea == "YES" or like_tea == "Y":
            print("Good for you. Give Coffee another try:)")
        elif like_tea == "NO" or like_tea == "N":
           print("I am sorry. That is all I have for now.")

    else:
        print("I don't understand. Please answer with yes and no.")

    keep_going = input("Press <enter> to continue or any other key to quit")
    '''

# Version 3.1
# create a funtion that I can use over and over again
# Makes my code Recylable
# The program will ask a person for a number and do something with it
# loop the program until a valid number gets entered
'''
def intcheck(question, low, high):  #Def creates a funtion. int check is the functions name.
    valid = False
    while not valid:
        error = f"Whoops, you have entered the wrong number. Please " \
        "Enter a valid interger between {low} and {high}."
        
    try:
        response = int(input(f"Enter and integer between {low} and {high}."))
        print(response)

        if response >=1 and response <=10
        print(f"you have entered {response}")
            valid = True
        
        else:
            print(error)



    except ValueError:
      print(error)

intcheck() # To call (use) the function, write out its name
'''

# Questions to ask the user
num1 = intcheck("Enter a number between 1 and 10", 1, 10) # To call (use) the funtion
num2 = intcheck("Enter a number between 15 and 20", 15, 20)

sum = num1 + num2
