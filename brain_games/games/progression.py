from random import randint
from brain_games.games_const import DESCRIPTION_progr, STEP_START, STEP_STOP
from brain_games.games_const import PR_LENG_STOP, PR_LENG_START, START, STOP_50

DESCRIPTION = DESCRIPTION_progr


def generate_question_and_answer():

    progression = []
    number = randint(START, STOP_50)
    step = randint(STEP_START, STEP_STOP)
    for _ in range(randint(PR_LENG_START, PR_LENG_STOP)):
        progression.append(number)
        number = number + step
    correct_answer = progression[randint(0, len(progression) - 1)]
    correct_answer_index = progression.index(correct_answer)
    progression[correct_answer_index] = '..'
    progression = ' '.join(map(str, progression))
    question = f'{progression}'
    return question, str(correct_answer)
