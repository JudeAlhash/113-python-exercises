# EX 104 : Make a function that will validate if the received value is an integer or not.

def readInt(a):
    while not a.isnumeric():
        a = str(input('Invalid input! Please enter any numeric value.'))
    a = int(a)
    return a


b = readInt(str(input('Give me a number:')))
print(f'The number given was {b}')