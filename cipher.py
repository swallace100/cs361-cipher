"""
Name: Steven Wallace
Class: CS361
Project: Microservice: Cipher
Description: Get an integer from the user and shifts the letters in the cipher-data.txt that many characters. Then return the data.
"""

import time
import os
import sys

"""
The Cipher gets an integer from the user and shifts the letters in the cipher-data.txt that many characters. 
Then return the data.
"""
def start_cipher():
    time.sleep(1)

    string_array = []
    user_input = 0
    valid_input = False
    
    print("")
    print("Cipher Microservice")
    print("")

    print("The Cipher gets an integer from the user and shifts the letters read from cipher-data.txt that many times.")
    print("Input 'x' or the word 'exit' to exit the program.")

    print("")
    print("Input an integer for the cipher:")

    while valid_input is False:
        user_input = input()
        try:
            # Check if the input can be convert into an int
            user_input_int = int(user_input)
            valid_input = True
        except ValueError:
            if user_input == "x":
                print("Thank you for using the Cipher. Goodbye.")
                sys.exit(0)
            elif user_input == "exit":
                print("Thank you for using the Cipher. Goodbye.")
                sys.exit(0)
            else:
                print("Please type a valid integer.")

    valid_input = False

    """
    Source: Shift letters by a certain value in python
    URL: https://stackoverflow.com/questions/48514673/shift-letters-by-a-certain-value-in-python 
    Usage: I used this as a reference to create the letter shift.
    """
    def shift_letters(letter, shift):
        
        new_letter = ord(letter) + shift
        if 'A' <= letter <= 'Z': 
            return chr((new_letter - ord('A')) % 26 + ord('A'))
        elif 'a' <= letter <= 'z': 
            return chr((new_letter - ord('a')) % 26 + ord('a'))
        else:
            print("Invalid character in input. Please make sure the input is alphabetic and try again.")
            sys.exit(0)

    cipher_num = int(user_input)

    path_dirname = os.path.dirname(__file__)
    file_path = os.path.join(path_dirname, "cipher-data.txt")

    with open(file_path, "r") as original_text:
        file_string = original_text.read()

    for char in file_string:
        string_array.append(char)

    for i in range(len(string_array)):
        string_array[i] = shift_letters(string_array[i], cipher_num)
    
    cipher_result = ''.join(string_array)
    print("The cipher shifted value is: " + cipher_result)

    file_path = os.path.join(path_dirname, "cipher-data.txt")
    with open(file_path, "w") as cipher_data:
        cipher_data.write(cipher_result)
    
    print("The shifted value has been written to cipher-data.txt")

    print("")
    print("Input a different number? [yes/no]")

    while valid_input is False :
        user_input = input()

        if user_input == "yes":
            start_cipher()
        elif user_input == "no":
            print("Thank you for using the Cipher. Goodbye.")
            sys.exit(0)
        elif user_input == "x":
            print("Thank you for using the Cipher. Goodbye.")
            sys.exit(0)
        elif user_input == "exit":
            print("Thank you for using the Cipher. Goodbye.")
            sys.exit(0)
        else:
            print("Please type a valid input.")


# Start the Cipher
start_cipher()