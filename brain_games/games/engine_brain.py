import random
from brain_games.games.cli import welcome_user


def engine_brain(function, game_description):
        k = 0
        name = welcome_user(game_description)
        while k < 3:
            question, answer = function()
            print(f'Question: {question}')
            answer_user = input('Your answer: ')
            if answer_user.isalnum() or answer_user[0] == '-':
                answer_user = int(answer_user)
            if answer == answer_user:
                print('Correct!')
                k += 1
            else:
                print(f"'{answer_user}' is wrong answer;(\n"
                      f"Correct answer was '{answer}'"
                      f"\nLet's try again, {name}")
                break
        else:
            print(f'Congratulations, {name}')
