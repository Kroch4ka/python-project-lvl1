from random import randint
from brain_games.games.cli import welcome_user


def prime_number(rand_number):
    a = True
    for k in range(2, rand_number):
        if rand_number % k == 0:
            a = False
    if a:
        return 'yes'
    return 'no'


def brain_prime():
    name = welcome_user('Answer "yes" if given number is prime. '
                        'Otherwise answer "no".')
    k = 0
    while k < 3:
        question = randint(2, 100)
        answer = prime_number(question)
        print(f'Question: {question}')
        user_answer = input('Your answer: ').lower()
        if user_answer == answer:
            print("Correct!")
            k += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'\nLet's try again, {name}")
            break
    else:
        print(f'Congratulations, {name}!')
