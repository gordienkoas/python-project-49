import random


from brain_games.games_const import CALC_INSTRUCTION
from brain_games.engine import run_game
from brain_games.utility import get_random_number


def get_rnd_math_sign_and_result(first_num, second_num):
    return random.choice([
        ('+', first_num + second_num),
        ('-', first_num - second_num),
        ('*', first_num * second_num)
    ])


def generate_question_and_answer():
    first_num, second_num = get_random_number(1, 10), get_random_number(1, 10)
    sign, correct_answer = get_rnd_math_sign_and_result(first_num, second_num)
    question = f"{first_num} {sign} {second_num}?"
    return question, str(correct_answer)


def run_calc_game():
    run_game(generate_question_and_answer, CALC_INSTRUCTION)
