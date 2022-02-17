# EX 085 : Make a script that will receive 7 values from the user, and separate them into evens and
# unevens within the same list, and then display them in order.
L = [[], []]
for c in range(0, 7):
    v = int(input('Give me a number.'))
    if v % 2 == 0:
        L[0].append(v)
    else:
        L[1].append(v)
L.sort()
print(L)

