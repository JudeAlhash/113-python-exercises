# EX 105 : Write a function that will receive many grades from a certain class, and store the following info
# into a dictionary: Total number of grades; Biggest grade; Smallest grade; Average of grades;
# Situation of the class (optional). Include docstrings.

def grades(*num, sit=False):
    big = small = num[0]
    ave = 0
    info = dict()
    info['total grades'] = len(num)
    for c, v in enumerate(num):
        ave += v
        if v == 0:
            big = small = v
        if v > big:
            big = v
        elif v < small:
            small = v
    info['biggest grade'] = big
    info['smallest grade'] = small
    info['average'] = (ave / len(num))
    if sit:
        if info['average'] >= 7:
            info['situation'] = 'Great!'
        elif info['average'] >= 4:
            info['situation'] = 'Bad.'
        else:
            info['situation'] = 'Terrible.'
    return info


classStatus = grades(3, 1, 3, 4, 5, sit=True)
print(classStatus)