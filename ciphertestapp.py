"""
Name: Steven Wallace
Class: CS361
Project: Microservice: Cipher Test App
Description: Small application that tests the cipher microservice.
"""

import time
import os
import sys

"""
The Cipher gets an string from the user and writes it to cipher-data.txt. The string will be used by the cipher. 
"""
def start_cipher_test():
    time.sleep(1)

    string_array = []
    user_input = 0
    valid_input = False
    
    print("")
    print("Cipher Test App")
    print("")

    print("This app tests the cipher. It writes user input to cipher-data.txt, which will be used by the cipher.")
    print("Input the number 0 to exit the program.")

    print("")
    print("Please input a word or alphabetic character:")
    

    while valid_input is False:
        user_input = input()

        if user_input == "0":
            print("Thank you for using the Cipher Test App. Goodbye.")
            sys.exit(0)
        elif not user_input.isalpha():
            print("Please only enter alphabetic words or characters.") 
        else:
            valid_input = True

    valid_input = False

    path_dirname = os.path.dirname(__file__)
    file_path = os.path.join(path_dirname, "cipher-data.txt")

    with open(file_path, "w") as cipher_data:
        cipher_data.write(user_input)
    
    print("The string: " + user_input + " has been written to cipher-data.txt")

    print("Input a different alphabetic word or character? [yes/no]")

    while valid_input is False :
        user_input = input()

        if user_input == "yes":
            start_cipher_test()
        elif user_input == "no":
            valid_input = True
        elif user_input == "0":
            print("Thank you for using the Cipher. Goodbye.")
            sys.exit(0)
        else:
            print("Please type a valid input.")

        
    valid_input = False
    print("")
    print("Would you like to see the cipher output? [yes/no]")
    while valid_input is False :
        user_input = input()

        if user_input == "yes":
            file_path = os.path.join(path_dirname, "cipher-data.txt")
            with open(file_path, "r") as cipher_output:
                file_string = cipher_output.read()
            print("The cipher ouput is: " + file_string)
            print("")
            valid_input = True
            
        elif user_input == "no":
            print("Thank you for using the Cipher. Goodbye.")
            sys.exit(0)
        elif user_input == "x":
            print("Thank you for using the Cipher. Goodbye.")
            sys.exit(0)
        elif user_input == "n":
            print("Thank you for using the Cipher. Goodbye.")
            sys.exit(0)
        elif user_input == "exit":
            print("Thank you for using the Cipher. Goodbye.")
            sys.exit(0)
        else:
            print("Please type a valid input.")


# Start the Cipher Test App
start_cipher_test()