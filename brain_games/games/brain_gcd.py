from random import randint


def gcd():
    gcd_value = 0
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    for k in range(1, min(num_1, num_2) + 1):
        if num_1 % k == 0 and num_2 % k == 0:
            gcd_value = k
            return ' '.join(map(str, [num_1, num_2])), gcd_value
