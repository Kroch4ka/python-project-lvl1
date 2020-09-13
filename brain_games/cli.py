# Module with input function

"""The welcome user function asks for a name and displays a greeting."""

import prompt

# The function asks for your name and greets

"""The function takes as input a name of type string and outputs greeting"""

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name} !")
