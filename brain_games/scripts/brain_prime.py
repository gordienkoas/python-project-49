import random
import math
from brain_games.cli import welcome_user


name = welcome_user()


def is_prime(number):
    # список простых чисел начинается с 2, всё остальное можно сразу отмести
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number))
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if number % element == 0:
            return False
    return True


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    for i in range(0, 3):
        check_number = random.randint(1, 99)
        x = is_prime(check_number)
        print('Question:', check_number, end=' ')
        answer = str(input())
        if x is True and answer == 'yes' or x is False and answer == 'no':
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
