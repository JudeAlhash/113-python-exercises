# EX 093 : Create a program that will read a soccer player's name, and how many matches he played this season.
# Then, ask how many goals he made in each game. Display in 3 different ways the components of this dictionary:
# Name, goals, and total goals.

stats = {'Name': str(input('Player name:')), 'goals': [], 'total': 0}
matches = int(input('How many matches were played?'))
for c in range(0, matches):
    stats['goals'].append(int(input(f'How many goals in match {c+1}?')))
    stats['total'] += stats['goals'][c]
print('-='*30)
print(stats)
print('-='*30)
for k, v in stats.items():
    print(f'{k}: {v}')
print('-='*30)
print(f'Player {stats["Name"]} played {matches} matches.')
for a, b in enumerate(stats['goals']):
    print(f'In match {a}, he scored {b} goals.')
print(f'The total goal count is {stats["total"]}.')
print('-='*30)