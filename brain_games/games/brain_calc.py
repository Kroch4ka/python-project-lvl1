import random
from operator import add, mul, sub, truediv


def calculation_operation():
    description = 'What is the result of the expression?'
    first_operand = random.randint(1, 100)
    second_operand = random.randint(1, 100)
    collection_operators = ['+', '-', '*', '/']
    operator = random.choice(collection_operators)
    associative_operators = {'+': add(first_operand, second_operand),
                             '-': sub(first_operand, second_operand),
                             '*': mul(first_operand, second_operand),
                             '/': round(truediv(first_operand, second_operand), 1)}
    result_operation = associative_operators[operator]
    question_for_player = f'{str(first_operand)} {operator} {str(second_operand)}'
    return question_for_player, result_operation, description
