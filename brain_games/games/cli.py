import prompt

def greet_user():
    print('Welcome to the Brain Games!')


def ask_name():
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name
