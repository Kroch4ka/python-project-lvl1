import random
import math


def get_operator_expression():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operations = ['+', '-', '*', '/']
    random_key_operation = operations[random.randint(0, len(operations) - 1)]
    dict_operations = {'+': number_1 + number_2,
                       '-': number_1 - number_2,
                       '*': number_1 * number_2,
                       '/': math.ceil(number_1 / number_2)}
    random_value_operation = dict_operations.get(random_key_operation)
    return ' '.join(map(str, [number_1, random_key_operation, number_2])), random_value_operation

