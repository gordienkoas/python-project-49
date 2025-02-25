from math import gcd
from brain_games.utility import get_random_number
from brain_games.engine import run_game


from brain_games.games_const import GCD_INSTRUCTION


def generate_question_and_answer():
    num1, num2 = get_random_number(10, 30), get_random_number(10, 50)
    question = f'{num1} {num2}'
    correct_answer = gcd(num1, num2)

    return question, str(correct_answer)


def run_gcd_game():
    run_game(generate_question_and_answer, GCD_INSTRUCTION)
