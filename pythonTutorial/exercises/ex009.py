# 009: Write a script that reads a number, then shows its multiplication chart.
c = int(input('I`ll multiply any number you need pal. Even if you don`t need it. Heh.'))
print('Here ya go.')
print(
    '{0} X 1 = {1} \n {0} X 2 = {2} \n {0} X 3 = {3} \n {0} X 4 = {4} \n {0} X 5 = {5} \n {0} X 6 = {6} \n {0} X 7 = {7} \n {0} X 8 = {8} \n {0} X 9 = {9} \n'.format(
        c, c * 1, c * 2, c * 3, c * 4, c * 5, c * 6, c * 7, c * 8, c * 9))
