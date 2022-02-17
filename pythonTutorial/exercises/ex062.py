# EX 62: Develop a program that reads a FIRST TERM and the REASON of a ARITHMETIC PROGRESSION.
# Then, show the 10 first terms of the progression, just like in ex 051, but using WHILE.
# Then, ask if they want to see any more numbers after the tenth, as many times as the user wants.
primeiro = int(input('Whats the first term of the progression?'))
razao = int(input('Whats the count rate of this progression?'))
count = primeiro
c = 1
limit = 10
while c <= limit:
    print('{}'.format(primeiro), end=' > ')
    primeiro += razao
    if c == limit:
        print('PAUSE!')
        limit += int(input('How many more terms of this progression do you wish to see?'))
    c += 1
print('Progression ended, with {} terms produced.'.format(limit+1))
