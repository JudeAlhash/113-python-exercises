# EX 61: Develop a program that reads a FIRST TERM and the REASON of a ARITHMETIC PROGRESSION.
# Then, show the 10 first terms of the progression, just like in ex 051, but using WHILE.
primeiro = int(input('Whats the first term of the progression?'))
razao = int(input('Whats the count rate of this progression?'))
count = primeiro
c = 0
while not primeiro >= (count+10)*razao:  # 10th number of an arithmetic progression: decimo = primeiro + (10-1) * razao
    print(primeiro)
    primeiro += razao
    c += 1
    if c >= 10:
        break
