
import random


def progression():
    len_progression = 10
    rand_step = random.randint(2, 8)
    list_of_ariphm = []
    while True:
        first_n = random.randint(1, 10)
        last_n = random.randint(1, 100)
        if (last_n - first_n) / rand_step == len_progression:
            for index, value in enumerate(range(first_n, last_n, rand_step)):
                list_of_ariphm.append(str(value))
            break
    replace_index = random.randint(0, 9)
    win_value = int(list_of_ariphm[replace_index])
    list_of_ariphm[replace_index] = ".."
    return ' '.join(list_of_ariphm), win_value



