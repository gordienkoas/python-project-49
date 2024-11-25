import random
import math


def welcome_user():
    global name
    print('May I have your name? ', end='')
    name = str(input())
    print(f'Hello, {name}')
    return name


def main():
    print('Find the greatest common divisor of given numbers.')
    count = 0
    x = 0
    for i in range(0, 3):
        rnd1 = random.randint(1, 99)
        rnd2 = random.randint(1, 99)
        print('Question:', rnd1, rnd2, end=' ')
        x = int(input())
        result = math.gcd(rnd1, rnd2)
        if result == x:
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f'{x} is wrong answer ;( .Correct answer was {result}.')
            print(f"Let's try again, {name}!")
            break


welcome_user()

if __name__ == '__main__':
    main()
