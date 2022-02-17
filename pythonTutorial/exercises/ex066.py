# EX 066: Create a program that will receive integer values from the user, until it receives 999. Then, show
# how many numbers were typed in, and what's their sum.

s = a = count = 0
while True:
    a = int(input('Type any number, or type 999 to exit.'))
    if a == 999:
        break
    s += a
    count += 1
print(f'The sum of all the {count} numbers is {s}')