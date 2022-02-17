# LESSON 17: LISTS! (PART 1)

l = [0, 1, 1, 8, 9]
print(l)
l.remove(9)
l.pop()
l.append(420)
l.append(6969)
l.insert(0, 1337)
del l[3]
print(l)
print('*'*30)
values = []
values.append(6)
values.append(9)
values.append(420)
print(values)
for c, v in enumerate(values):
    print(f'{c, v}...', end='')

valores = list()
for cont in range(1, 10):
    valores.append(int(input('Give me your numbers! All of them !!!!')))
print(valores)

