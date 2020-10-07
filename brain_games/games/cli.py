import prompt

def greets_the_user(*game_template):
    print('Welcome to the Brain Games!')
    dictionary_of_description_games = {'formatting_even_game': 'Answer "yes" if number '
                                                               'even otherwise answer "no"\n\n',
                                       'calculation_operation': 'What is the result '
                                                                'of the expression?\n\n',
                                       'formatting_gcf': 'Find the greatest common '
                                                         'divisor of given numbers.\n\n',
                                       'formatting_progression': 'What number is missing '
                                                                 'in the progression?\n\n',
                                       'formatting_prime': 'Answer "yes" if given number '
                                                           'is prime. Otherwise answer "no".\n\n'}

    if game_template:
        print(dictionary_of_description_games.get(game_template.__name__))


def asking_name():
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!\n\n')
    return player_name
