import random

def getting_progression():
    random_step = random.randint(1, 9)
    random_ariph = range(1, 100, random_step)
    result_progression = [str(value) for index, value in enumerate(random_ariph) if index < 10]
    return result_progression

def formatting_progression():
    description = 'What number is missing in the progression'
    ariph_progression = getting_progression()
    winning_index = random.randint(0, len(ariph_progression) - 1)
    winning_value = ariph_progression[winning_index]
    ariph_progression[winning_index] = '..'
    formatting_progression = ' '.join(ariph_progression)
    return formatting_progression, winning_value, description
