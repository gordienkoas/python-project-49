from random import choice, randint

from brain_games.games_const import DESCRIPTION_calc, START, STOP

DESCRIPTION = DESCRIPTION_calc


def generate_question_and_answer():

    operation = choice(['+', '-', '*'])
    num_1 = randint(START, STOP)
    num_2 = randint(START, STOP)
    question = f'{num_1} {operation} {num_2}'
    if operation == '+':
        correct_answer = num_1 + num_2
    elif operation == '-':
        correct_answer = num_1 - num_2
    elif operation == '*':
        correct_answer = num_1 * num_2
    return question, str(correct_answer)
