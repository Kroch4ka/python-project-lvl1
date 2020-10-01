
from brain_games.games.brain_calc import get_operator_expression
from brain_games.games.engine_brain import engine_brain


def main():
    engine_brain(get_operator_expression, 'What is the result of the expression?')

if __name__  == '__main__':
    main()
