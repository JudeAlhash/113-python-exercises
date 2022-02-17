#LESSON 18 LISTS WITHIN LISTS
data = []
peeps = []
for c in range(0, 5):
    data.append(str(input('What is your name?')))
    data.append(str(input('How old are you?')))
    peeps.append(data[:])
    data.clear()
    print(peeps)