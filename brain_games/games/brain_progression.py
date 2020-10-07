import random

def getting_progression():
    result_progression = []
    step_progression = random.randint(1, 7)
    for k in range(1, 100, step_progression):
        if len(result_progression) < 10:
            result_progression.append(k)
        else:
            return result_progression


def formatting_progression():
    ariph_progression = getting_progression()
    winning_index = random.randint(0, 9)
    winning_value = ariph_progression[winning_index]
    ariph_progression[winning_index] = '..'
    formatting_progression = ' '.join(map(str, ariph_progression))
    return formatting_progression, winning_value
