from random import choice

from brain_games.games_const import DESCRIPTION_calc
from brain_games.engine import play
from brain_games.utility import get_random_number


def generate_question_and_answer():

    operation = choice(['+', '-', '*'])
    num_1 = get_random_number(1,10)
    num_2 = get_random_number(1, 10)
    question = f'{num_1} {operation} {num_2}'
    if operation == '+':
        correct_answer = num_1 + num_2
    elif operation == '-':
        correct_answer = num_1 - num_2
    elif operation == '*':
        correct_answer = num_1 * num_2
    return question, str(correct_answer)

def run_calc_game():
    play(generate_question_and_answer, DESCRIPTION_calc)