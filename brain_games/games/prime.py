from brain_games.games_const import PRIME_INSTRUCTION
from brain_games.utility import get_random_number
from brain_games.engine import play


def generate_question_and_answer():

    def is_prime(num):
        if num < 2:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True

    number = get_random_number(1, 100)
    question = f'{number}'

    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer


def run_prime_game():
    play(generate_question_and_answer, PRIME_INSTRUCTION)
