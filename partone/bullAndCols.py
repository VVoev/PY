# Libs
import random

# GET GUESS


def get_guess():
    return list(input('Enter your guess '))

# GENERATE COMPUTER CODE


def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:4]

# GENERATE CLUES


def generate_clues(code, user_guess):
    if code == user_guess:
        return 'You Win'

    clues = []
    for index, num in enumerate(user_guess):
        if num == code[index]:
            clues.append('Bull')
        elif num in code:
            clues.append('Cow')

    if clues == []:
        return 'Nothing'
    else:
        return clues


# Game Logic
secret_code = generate_code()
clue_report = []
while clue_report != 'You win':
    guess = get_guess()

    clue_report = generate_clues(guess, secret_code)
    for clue in clue_report:
        if clue == 'You win':
            print('You Win')
            exit()
        else:
            print(clue)


# TEST
generate_code()
