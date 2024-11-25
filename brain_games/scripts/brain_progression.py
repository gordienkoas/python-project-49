from brain_games.cli import welcome_user
import random


name = welcome_user()


def main():
    print('What number is missing in the progression?')
    count = 0
    for i in range(0, 3):
        ls = []
        start_progr = random.randint(2, 20)
        num_progr = random.randint(3, 5)
        for i in range(10):
            hide_elem = random.randint(1, 9)
            ls.append(start_progr + num_progr)
            start_progr += num_progr
        cor_answer = ls[hide_elem]
        ls[hide_elem] = '..'
        print('Question:', *ls, end=' ')
        x = int(input())
        if x == cor_answer:
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
                break
        else:
            print(f'{x} is wrong answer ;(.Correct answer was {cor_answer}.')
            print(f"Let's try again, {name}!")
            break


if __name__ == '__main__':
    main()
