# Module with input function

"""The welcome user function asks for a name."""

import prompt

# The function asks for your name and greets

"""The function takes as input"""



def welcome_user():
    name = prompt.string('May I have your name? ')
    greeting = 'Hello, {}'.format(name)
    print(greeting)
