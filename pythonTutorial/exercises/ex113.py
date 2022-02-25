def readInt(a):
    while True:
        try:
            n = int(input(a))
        except (TypeError, ValueError):
            print('Type in an Integer Number')
            continue
        else:
            return a


b = readInt(str(input('Give me a number:')))
print(f'The number given was {b}')