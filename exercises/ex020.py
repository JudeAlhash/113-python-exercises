
import random
# 020. Now, help the teacher find a random order for his students to present his papers
x1 = str(input('First student:'))
x2 = str(input('Second student:'))
x3 = str(input('Third student:'))
x4 = str(input('Fourth Student:'))
lista = [x1, x2, x3, x4]
random.shuffle(lista)
print(lista)


