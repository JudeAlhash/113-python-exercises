# EX 51: Develop a program that reads a FIRST TERM and the REASON of a ARITHMETIC PROGRESSION.
# Then, show the 10 first terms of the progression.

f = int(input('Whats the first term of the progression?'))
r = int(input('Whats the count rate of this progression?'))
count = 0
for c in range(f, (f + (10-1) * r) + r, r):
#    count += 1
#    if count <= 10:
    print(c, end=' - ')
print('END  .')


# formula to find 10th number of an arithmetic progression: decimo = primeiro + (10-1) * razao