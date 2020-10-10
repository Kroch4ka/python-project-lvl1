import random


def is_even(number):
    return number % 2 == 0


def formatting_even_game():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    operand = random.randint(1, 100)
    if is_even(operand):
        return operand, 'yes', description
    return operand, 'no', description
