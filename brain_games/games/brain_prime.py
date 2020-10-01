import random

def prime_number():
    rand_number = random.randint(2, 100)
    a = True
    for k in range(2, rand_number):
        if rand_number % k == 0:
            a = False
    if a:
        return rand_number, 'yes'
    return rand_number, 'no'
