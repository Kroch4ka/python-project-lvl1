import random


def is_prime(number):
    if number == 2:
        return True
    for k in range(2, number):
        if number % k == 0:
            return False
    return True


def formatting_prime():
    check_number = random.randint(2, 100)
    if is_prime(check_number):
        return check_number, 'yes'
    return check_number, 'no'
