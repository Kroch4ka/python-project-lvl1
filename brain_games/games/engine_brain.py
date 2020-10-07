from brain_games.games.cli import greets_the_user, asking_name

def interact_with_player(game_template):
        greets_the_user(game_template)
        name = asking_name()
        for k in range(3):
            question, answer = game_template()
            print(f'Question: {question}')
            answer_user = input('Your answer: ')
            if str(answer) == answer_user:
                print('Correct!')
            else:
                print(f"'{answer_user}' is wrong answer;(\n"
                      f"Correct answer was '{answer}'"
                      f"\nLet's try again, {name}")
                break
        else:
            print(f'Congratulations, {name}')
