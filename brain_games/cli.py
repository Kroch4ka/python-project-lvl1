# Module with input function

"""The welcome user function asks for a name."""

import prompt
import random
# The function asks for your name and greets

"""The function takes as input"""


def welcome_user():
    print('Welcome to the Brain Games\nAnswer "yes" if number even otherwise answer "no".\n\n')
    name = prompt.string('May I have your name? ')
    greeting = 'Hello, {}\n\n'.format(name)
    print(greeting)
