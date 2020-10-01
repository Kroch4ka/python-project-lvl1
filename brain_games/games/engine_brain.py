from brain_games.games.cli import welcome_user


def engine_brain(function, game_description):
        """General engine for subsequent text games
        Input: a wrap-around game(function) that should
        return an appropriate question for the player and an answer,
        description of the game(string format)
        Output: based on the received data,
        organizes a simple game with the player"""
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
