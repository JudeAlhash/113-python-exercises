# EX 084 : Make a script that will read peoples NAMES and WEIGHTS, put them into separate lists, and then show
# how many people are in the list, what's the biggest and smallest value between them, and list the poeple
# that have those weights.
data = []
peeps = []
bigList = []
smallList = []
b = s = c = 0
while True:
    data.append(str(input('Name?')))
    data.append(int(input('Weight?')))
    print(data)
    if c == 0:
        s = data[1]
    if data[1] >= b:
        b = data[1]
    elif data[1] <= s:
        s = data[1]
    peeps.append(data[:])
    data.clear()
    c += 1
    check = str(input('Input [NO] if you would like to quit.')).strip().lower()[0]
    if check == 'n':
        break
for i in peeps:
    if i[1] == b:
        bigList.append(i[0])
    if i[1] == s:
        smallList.append(i[0])
print(f'There are a total of {len(peeps)} people, the heaviest being {b}kg {bigList},'
      f' and the lightest being {s}kg {smallList}.')