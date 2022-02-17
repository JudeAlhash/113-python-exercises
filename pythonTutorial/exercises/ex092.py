# EX 092 : Make a script that will receive the following values from the user and put them into a dictionary:
# Name, Birth Year, Work Permit, and if Work Permit is different from 0:
# the Dictionary will also receive the Year the person was hired, and the salary.
# Then, find out when the person can retire.
from datetime import datetime
workInfo = {'name': str(input('Name?')),
            'birth year': int(input('Year of birth?')),
            'work permit': int(input('Work permit number: [0 if none]'))}
workInfo['age'] = datetime.now().year - workInfo['birth year']
if workInfo['work permit'] != 0:
    workInfo['hire year'] = int(input('What year were you hired?'))
    workInfo['salary'] = int(input('What is your salary?'))
    workInfo['retirement'] = (workInfo['hire year'] + 35) - workInfo['birth year']
for k, v in workInfo.items():
    print(f'{k}:{v}')

