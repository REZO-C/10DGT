# Area and Perimiter assesment
# Caleb
# 16/5/2025
# Version 1

Height = 0
Width = 0
     
    # This asks for the Height and Width
Height = int(input("Please enter the Height: "))

     # tests the height if it is above 0
while Height <=0:
    Height = int(input("Error: Please enter the Height (the number must be above 0): "))

Width = int(input("Please enter the Width: "))   

     # tests the Width if it is above 0
while Width <= 0:
    Width = int(input("Error: Please enter the Width (the number must be above 0): "))


    # Printing the chosen Height and Width
print(f"The height you chose was: {Height}")
print(f"The width you  chose was: {Width}")

    # Calculates and displays the Area
Area = Height * Width
print(f"This is the area {Area}")

    # Calculates and displays the Perimeter
Perimeter = Height + Width + Height + Width
print(f"This is the Perimeter {Perimeter}")

     # When you press enter the code quits
user_input = input(f"Press 'enter' to quit")
if user_input == 'enter':
    exit()