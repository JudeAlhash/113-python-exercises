# EX 060: write a script that will read a value and show its factor.
n = int(input('Give me a number to factor.'))
c = n
while c > 0:
    c -= 1
    if c > 0:
        n = n * c
print(n)

n2 = int(input('Give me another number to factor.'))
c2 = n2
for f in range(c2-1, 1, -1):
    c2 *= f
print(c2)