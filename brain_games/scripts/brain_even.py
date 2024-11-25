import random
from brain_games.cli import welcome_user


name = welcome_user()


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    for i in range(0, 3):
        rnd = random.randint(1, 99)
        print('Question:', rnd)
        print('Your answer:', end=' ')
        x = str(input())
        if (rnd % 2 == 0 and x == 'yes') or (rnd % 2 != 0 and x == 'no'):
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
                break
        else:
            if x == 'yes':
                print("'yes' is wrong answer ;( .Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
            else:
                print("'no' is wrong answer ;( .Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break



if __name__ == '__main__':
    main()
