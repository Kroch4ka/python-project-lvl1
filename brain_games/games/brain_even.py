import prompt
import random
from brain_games.games.cli import welcome_user


def parity_check():
    name = welcome_user('Answer "yes" if number even otherwise answer "no"')
    n = 0
    while n < 3:
        question = random.randint(1, 100)
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ').lower()
        if question % 2 == 0 and answer.lower() == "yes":
            print("Correct!")
            n += 1
        elif question % 2 != 0 and answer.lower() == "no":
            print("Correct!")
            n += 1
        else:
            if question % 2 == 0:
                print("'{}' is wrong answer ;(. Correct answer was '{}'."
                      "\nLet's try again, {}!".format(answer, "yes", name))
                break
            else:
                print("'{}' is wrong answer ;(. Correct answer was '{}'."
                      "\nLet's try again, {}!".format(answer, "no", name))
                break
    else:
        print(f"Congratulations, {name}!")
