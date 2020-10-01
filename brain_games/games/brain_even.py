import random


def brain_even():
    random_number = random.randint(2, 100)
    if random_number % 2 == 0:
        return random_number, 'yes'
    return random_number, 'no'
