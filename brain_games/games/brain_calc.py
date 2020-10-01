import random
import math


def get_operator_expression():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operations = ['+', '-', '*', '/']
    random_index_operations = random.randint(0, len(operations) - 1)
    random_key_operation = operations[random_index_operations]
    dict_operations = {'+': number_1 + number_2,
                       '-': number_1 - number_2,
                       '*': number_1 * number_2,
                       '/': math.ceil(number_1 / number_2)}
    random_value_operation = dict_operations.get(random_key_operation)
    random_question = ' '.join([str(number_1), random_key_operation, str(number_2)])
    return random_question, random_value_operation
