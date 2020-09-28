import prompt
# The function asks for your name and greets


def welcome_user(a=" "):
    if a:
        print(f'Welcome to the Brain Games!\n{a}')
        name = prompt.string('\n\nMay I have your name? ')
        greeting = 'Hello, {}\n\n'.format(name)
        print(greeting)
        return name
