import random


def getting_gcf(first_operand, second_operand):
    dividend = 1
    min_operand = min(first_operand, second_operand)
    max_operand = max(first_operand, second_operand)
    for value in range(1, min_operand):
        if min_operand % value == 0 and max_operand % value == 0:
            dividend = value
    return dividend


def formatting_gcf():
    description = 'Find the greatest common divisor of given numbers.'
    random_first_operand = random.randint(1, 100)
    random_second_operand = random.randint(1, 100)
    dividend = getting_gcf(random_first_operand, random_second_operand)
    return str(random_first_operand) + ' ' + str(random_second_operand), dividend, description
