# Write a script that reads a number and tells me if it`s a prime number or not.
n = int(input('Type in any number.'))
prime = 0
for c in range(1, n+1):
    if n % c == 0:
        prime += 1
        print('\033[0;32m{}\033[m'.format(c), end=' ')
    else:
        print('\033[0;31m{}\033[m'.format(c), end=' ')
if prime == 2:
    print('\nThe received number is a PRIME number.')
else:
    print('\nThe received value is not a prime number, and it is divisible by {} number(s).'.format(prime))
