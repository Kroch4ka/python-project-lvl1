import random


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    for k in range(2, number):
        if number % k == 0:
            return False
    return True


def formatting_prime():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    check_number = random.randint(2, 100)
    if is_prime(check_number):
        return check_number, 'yes', description
    return check_number, 'no', description
