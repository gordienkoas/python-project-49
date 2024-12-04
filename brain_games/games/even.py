from random import randint

from brain_games.games_const import START, STOP_100, DESCRIPTION_even

DESCRIPTION = DESCRIPTION_even


def generate_question_and_answer():

    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

    number = randint(START, STOP_100)
    question = f'{number}'

    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
