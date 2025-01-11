from brain_games.games_const import DESCRIPTION_even
from brain_games.utility import get_random_number
from brain_games.engine import play

DESCRIPTION = DESCRIPTION_even


def generate_question_and_answer():

    def is_even(number):
        return number % 2 == 0

    number = get_random_number(1, 100)
    question = f'{number}'



    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer

def run_even_game():
    play(generate_question_and_answer, DESCRIPTION)