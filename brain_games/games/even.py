from brain_games.games_const import EVEN_INSTRUCTION
from brain_games.utility import get_random_number
from brain_games.engine import play


def is_even(num):
    return num % 2 == 0


def generate_question_and_answer():
    number = get_random_number(1, 100)
    question = f'{number} is even. yes or no?'

    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer


def run_even_game():
    play(generate_question_and_answer, EVEN_INSTRUCTION)
