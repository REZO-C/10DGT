# Bits Calculator
# Author Caleb Prestidge
# Date 30/5/2025
# Version 1
def integers():
    while True:
        try:
            # This asks for the number/integer
            bit = int(input("Enter in a number (it must be above 0): "))
            if bit > 0:
                # This tells the user the bits required
                print(f"The bits required to process this are: {bit.bit_length()}")
                break
            else:
                print("Please enter a number that is bigger than 0.")
        except ValueError:
            # this is the error message
            print("Error! Please enter in an number.")

def texts():
    # This asks the user to put in some text
    text = input("Please enter in some text: ")
    # This tells the user the bits required
    print(f"The bits required to process this are: {len(text) * 8}")

def image():
    # This asks for the width and height of the image
    width = int(input("Please enter in the image width: "))
    height = int(input("Please enter in the image height: "))
    # This tells the user the bits required
    print(f"The bits required to process this are: {width * height * 24}")

def main():
    while True:
        option = input("Please choose to type in either an integer, an image, some text or type 'exit' to exit: ").lower()
        if option == "exit":
            print("Have a good day Thanks for playing!")
            break
        elif option == "integer":
            integers()
        elif option == "text":
            texts()
        elif option == "image":
            image()
        else:
            print("Error please enter in an integer, an image, some text or type 'exit' to exit")

if __name__ == "__main__":
    main()