from brain_games.games.cli import welcome_user
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
    win_value = list_of_ariphm[replace_index]
    list_of_ariphm[replace_index] = ".."
    return win_value, list_of_ariphm


def brain_progression():
    name = welcome_user('What number is missing in the progression?')
    k = 0
    while k < 3:
        answer_question, list_of_ariphm = progression()
        print(f"Question: {' '.join(list_of_ariphm)}")
        answer_of_user = int(input("Your answer: "))
        if answer_of_user == int(answer_question):
            print("Correct!")
            k += 1
        else:
            print(f"'{answer_of_user}' is wrong answer ;(. "
                  f"Correct answer was '{answer_question}"
                  f"'\nLet's try again, {name}")
            break
    else:
        print(f"Congratulations, {name}!")
