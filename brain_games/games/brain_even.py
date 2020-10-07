import random


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def formatting_even_game():
    operand = random.randint(1, 100)
    if is_even(operand):
        return operand, 'yes'
    return operand, 'no'
