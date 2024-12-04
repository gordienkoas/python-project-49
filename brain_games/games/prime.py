from random import randint

from brain_games.games_const import START, STOP_100, DESCRIPT_prime

DESCRIPTION = DESCRIPT_prime


def generate_question_and_answer():

    def is_prime(n):

        if n == 1 or n == 0:
            return False

        for i in range(2, (int(n**0.5) + 1)):
            if n % i == 0:
                return False
        return True

    number = randint(START, STOP_100)
    question = f'{number}'

    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
