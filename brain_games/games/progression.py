from brain_games.utility import get_random_number
from brain_games.games_const import PROGRESSION_INSTRUCTION
from brain_games.engine import run_game


def generate_question_and_answer():

    progression = []
    number = get_random_number(1, 50)
    step = get_random_number(1, 5)
    for _ in range(get_random_number(10, 10)):
        progression.append(number)
        number = number + step
    correct_answer = progression[get_random_number(1, len(progression) - 1)]
    correct_answer_index = progression.index(correct_answer)
    progression[correct_answer_index] = '..'
    progression = ' '.join(map(str, progression))
    question = f'{progression}'
    return question, str(correct_answer)


def run_progr_game():
    run_game(generate_question_and_answer, PROGRESSION_INSTRUCTION)
