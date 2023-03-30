
#Write a Python class which has two methods get_String and print_String. 
#get_String accept a string from the user and print_String print the string in upper case#

import random

class Sauce:
    def __init__(self):
        self.user_string = ""

    def get_String(self):
        music_genres = ["rock", "jazz", "blues", "reggae", "hip hop", "country"]
        self.user_string = f"My favorite music genre is {random.choice(music_genres)}."

    def print_String(self):
        print(self.user_string.upper())

string_manipulator = Sauce()

# First run
string_manipulator.get_String()
string_manipulator.print_String()

# Redo the string
string_manipulator.get_String()
string_manipulator.print_String()