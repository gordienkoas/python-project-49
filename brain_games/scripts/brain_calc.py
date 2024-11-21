import random


def welcome_user():
    global name
    print('May I have your name? ', end='')
    name = str(input())
    print(f'Hello, {name}')
    return name

def main():
    print('What is the result of the expression?')
    count = 0
    x = 0
    for i in range(0, 3):
        rnd1 = random.randint(1, 10)
        rnd2 = random.randint(1, 10)
        if rnd1 < rnd2:
            rnd1, rnd2 == rnd2, rnd1
        rnd_op = random.choice(['-','+','*'])
        print('Question:', rnd1,rnd_op,rnd2, end=' ')
        x = int(input())
        if rnd_op == '+' and rnd1 + rnd2 == x:
            print('Correct!')
            count += 1
        elif rnd_op == '-' and rnd1 - rnd2 == x or rnd2 - rnd1 == x:
            print('Correct!')
            count += 1
        elif rnd_op == '*' and rnd1 * rnd2 == x:
            print('Correct!')
            count += 1
        else:
            if rnd_op == '+':
                sum = rnd1 + rnd2
                print(f'{x} is wrong answer ;( .Correct answer was {sum}.')
                print(f"Let's try again, {name}!")
                break
            elif rnd_op == '-':
                raznica = rnd1 - rnd2
                print(f'{x} is wrong answer ;( .Correct answer was {raznica}.')
                print(f"Let's try again, {name}!")
                break
            else:
                proizved = rnd1 * rnd2
                print(f'{x} is wrong answer ;( .Correct answer was {proizved}."')
                print(f"Let's try again, {name}!")
                break

    if count == 3:
        print(f'Congratulations, {name}!')


welcome_user()

if __name__ == '__main__':
    main()