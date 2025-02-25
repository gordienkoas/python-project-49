from brain_games.games_const import EVEN_INSTRUCTION
from brain_games.utility import get_random_number
from brain_games.engine import run_game


def is_even(num):
    return num % 2 == 0


def generate_question_and_answer():
    number = get_random_number(1, 100)
    question = f'{number} is even. yes or no?'
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer


def run_even_game():
    run_game(generate_question_and_answer, EVEN_INSTRUCTION)
