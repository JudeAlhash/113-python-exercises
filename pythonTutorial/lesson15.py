# Break Command, infinite loops
s = a = 0
while True:
    a = int(input('Type any number, or tyoe 999 to exit.'))
    if a == 999:
        break
    s += a
print(f'The sum of all the typed numbers is {s}')