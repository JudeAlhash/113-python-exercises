# EX 067: T A B U A D A v3 - MULTIPLICATION BOARD
while True:
    a = int(input('What number do you want to see in the MULTIPLICATION BOARD?\nA NEGATIVE VALUE WILL END THE PROGRAM.'))
    if a < 0:
        print('Farewell!')
        break
    print('\nMULTIPLICATION BOARD')
    print('='*25)
    for c in range(0, 10):
        print(f'{a} X {c+1} = {a * (c+1)}')
    print('=' * 25)