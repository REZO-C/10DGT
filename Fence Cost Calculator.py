# Fence Cost Calculator
# Author Caleb Prestidge
# Date: 23/5/2025
# Version 1

height = 0
width = 0
cost = 0
     
    # This asks for the Height
height = float(input("Please enter the Height: "))
    # This asks for the Width

     # tests the height if it is above 0
while height <=0:
    height = float(input("Error: Please enter the Height (the number must be above 0): "))

width = float(input("Please enter the Width: "))     
     # tests the Width if it is above 0
while width <= 0:
    width = float(input("Error: Please enter the Width (the number must be above 0): "))

cost = float(input("Please choose the cost for the fencing: "))
    
     # this tests the cost if it is above 0 or a number
while cost <=0:
    cost = float(input("Error: Please enter the cost (it must be a number above 0): "))
    
    # Printing the chosen Height and Width
print(f"The height you chose was: {height}")
print(f"The width you chose was: {width}")

    # Calculates and displays the Area
area = round((height * width),2)
print(f"This is the area {area}")

    # Calculates and displays the Perimeter
perimeter = round((height + width + height + width),2)
print(f"This is the perimeter {perimeter}")


    # Calculates the cost for the perimeter and displays it
perimetercost = round((perimeter * cost),2)
print(f"This is the cost for the fence you: ${perimetercost}")

 # When you press enter the code quits
user_input = input(f"Press 'enter' to quit")
if user_input == 'enter':
    exit()