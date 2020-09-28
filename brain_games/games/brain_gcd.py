from random import randint
from brain_games.games.cli import welcome_user


def gcd(num_1, num_2):
    gcd_value = 0
    for k in range(1, min(num_1, num_2) + 1):
        if num_1 % k == 0 and num_2 % k == 0:
            gcd_value = k
    return gcd_value


def brain_gcd():
    name = welcome_user('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        result = gcd(num_1, num_2)
        print(f'Question: {num_1} {num_2}')
        answer = int(input('Your answer: '))
        if result == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'\n"
                  f"Let's try again, {name}")
            break
    else:
        print(f"Congratulations, {name}!")
