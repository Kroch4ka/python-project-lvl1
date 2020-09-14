
import prompt
import random



def parity_check():
        n = 0
        while n < 3:
            question = random.randint(1, 100)
            name_question = print('Question: {}\n'.format(question))
            answer = prompt.string('Your answer: ')
            if question % 2 == 0 and answer.lower() == "yes":
                print("Correct!")
                n += 1
            elif question % 2 != 0 and answer.lower() == "no":
                print("Correct!")
                n += 1
            else:
                if question % 2 == 0:
                    print("'{}' is wrong answer ;(. Correct answer was '{}'.\nLet's try again, Bill!".format(answer, "yes"))
                    break
                else:
                    print("{} is wrong answer ;(. Correct answer was '{}'.\nLet's try again, Bill!".format(answer, "no"))
                    break
        else:
            print("Congratulations, Bill!")
