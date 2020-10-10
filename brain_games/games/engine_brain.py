from brain_games.games.cli import greet_user, ask_name
from prompt import string


def launch_game(game_template):
        greet_user()
        name = ask_name()
        _, _, description_game = game_template()
        print(description_game)
        for number_of_rounds in range(3):
            question, answer, _ = game_template()
            print(f'Question: {question}')
            answer_user = string('Your answer: ')
            if ''.join(map(str, str(answer))) == answer_user:
                print('Correct!')
            else:
                print(f"'{answer_user}' is wrong answer;(\n"
                      f"Correct answer was '{answer}'"
                      f"\nLet's try again, {name}")
                break
        else:
            print(f'Congratulations, {name}')
