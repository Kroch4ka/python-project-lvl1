import random
from brain_games.games.cli import welcome_user


def get_operator_expression(arg_1, arg_2):
    c = random.randint(1, 3)
    dict_of_operations = {1: arg_1 + arg_2, 2: arg_1 * arg_2, 3: arg_1 - arg_2}
    if c == 1 in dict_of_operations:
        print(f"Question: {arg_1} + {arg_2}")
        return arg_1 + arg_2
    elif c == 2 in dict_of_operations:
        print(f"Question: {arg_1} * {arg_2}")
        return arg_1 * arg_2
    elif c == 3 in dict_of_operations:
        print(f"Question: {arg_1} - {arg_2}")
        return arg_1 - arg_2


def brain_calc():
    name = welcome_user('What is the result of the expression?')
    k = 0
    while k < 3:
        op_1 = int(random.randint(1, 100))
        op_2 = int(random.randint(1, 100))
        result = get_operator_expression(op_1, op_2)
        answer = int(input("Your answer: "))
        if answer == result:
            print("Correct!")
            k += 1
        else:
            print(f"\n'{answer}' is wrong answer;(."
                  f"Correct answer was '{result}'.\nLet's try again")
            break
    else:
        print(f"Congratulations, {name}!")
