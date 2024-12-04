from math import gcd
from random import randint
from brain_games.games_const import START, STOP, DESCRIPTION_gcd


DESCRIPTION = DESCRIPTION_gcd


def generate_question_and_answer():
    num1, num2 = randint(START, STOP), randint(START, STOP)
    question = f'{num1} {num2}'
    correct_answer = gcd(num1, num2)

    return question, str(correct_answer)
