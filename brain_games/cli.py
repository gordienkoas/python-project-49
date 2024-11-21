def welcome_user():
    global name
    print('May I have your name? ', end='')
    name = str(input())
    print(f'Hello, {name}')
    return name
