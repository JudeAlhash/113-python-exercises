# List inside a tuple the names of all the brazilian soccer teams in the Brazilian Championship Table. (There are 20.)
# Then, show me the first 5 teams, the last 4 teams, the tams in alphabetical order, and Chapecoense's position.
teams = ('Atletico Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza',
         'Corinthians', 'Bragantino', 'Fluminense', 'America',
         'Atletico GO', 'Santos', 'Ceara', 'Internacional',
         'Sao Paulo', 'Atletico Paranaense', 'Cuiaba', 'Juventude',
         'Gremio', 'Bahia', 'Sport', 'Chapecoense')
print('=--'*20)
print(f'The first five teams of the Championship are {teams[0:5]}.')
print('=--'*20)
print(f'The last four teams are {teams[16:]}')
print('=--'*20)
print(f'These are the teams in alphabetical order: {sorted(teams)}')
print('=--'*20)
print(f' Chapecoense is in the position number {teams.index("Chapecoense")+1}.')
print('=--'*20)
