"""
Name: Steven Wallace
Class: CS361
Project: Microservice: Cipher Test App
Description: Small application that tests the cipher microservice.
"""

import time
import os
import sys

def get_user_input():
    while True:
        user_input = input()
        if user_input == "0":
            print("Thank you for using the Cipher Test App. Goodbye.")
            sys.exit(0)
        elif not user_input.isalpha():
            print("Please only enter alphabetic words or characters.")
        else:
            return user_input

def write_to_file(file_path, data):
    with open(file_path, "w") as cipher_data:
        cipher_data.write(data)

def read_from_file(file_path):
    with open(file_path, "r") as cipher_output:
        return cipher_output.read()

def ask_user_to_continue():
    while True:
        user_input = input().lower()
        if user_input == "yes":
            return True
        elif user_input in ["no", "0"]:
            print("Thank you for using the Cipher. Goodbye.")
            sys.exit(0)
        else:
            print("Please type a valid input.")

def ask_to_see_output(file_path):
    while True:
        user_input = input().lower()
        if user_input == "yes":
            file_string = read_from_file(file_path)
            print("The cipher output is: " + file_string)
            print("")
            return
        elif user_input in ["no", "x", "n", "exit"]:
            print("Thank you for using the Cipher. Goodbye.")
            sys.exit(0)
        else:
            print("Please type a valid input.")

def start_cipher_test():
    time.sleep(1)
    print("\nCipher Test App\n")
    print("This app tests the cipher. It writes user input to cipher-data.txt, which will be used by the cipher.")
    print("Input the number 0 to exit the program.\n")
    print("Please input a word or alphabetic character:")

    user_input = get_user_input()

    path_dirname = os.path.dirname(__file__)
    file_path = os.path.join(path_dirname, "cipher-data.txt")

    write_to_file(file_path, user_input)
    print("The string: " + user_input + " has been written to cipher-data.txt")

    print("Input a different alphabetic word or character? [yes/no]")
    if ask_user_to_continue():
        start_cipher_test()

    print("\nWould you like to see the cipher output? [yes/no]")
    ask_to_see_output(file_path)

# Start the Cipher Test App
start_cipher_test()