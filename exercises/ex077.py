# EX 077 : Create a program that has a tuple with many words inside it. Separate the vowels from each of those words.
# Success!!!!!!!
tup = ('Catch', 'Maine', 'Brush',
       'Computer', 'Joao', 'Maria',
       'Videogame', 'Mother', 'Board')
for c in tup:
    print(f'In the word {c} we have the following vowels:', end='')
    for v in c:
        if v.lower() in 'aeiou':
            print(' ', v, end='')
    print('')
