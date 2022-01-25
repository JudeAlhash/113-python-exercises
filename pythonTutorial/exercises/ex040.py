#Find the average between the students grades, and reveal if he has passed or failed the class.

g1 = float(input('What was your first grade?'))
g2 = float(input('What was your second grade?'))

avg = (g1+g2)/2

if 6 <= avg < 7.5:
    print('Your grades are barely passable, averaging at {:.2f}. Congratulations, but do better.'.format(avg))
elif avg >= 7.5:
    print('Congratulations, you pass! Your grades were excellent, averaging {:.2f}'.format(avg))
else:
    print('Sorry, you did not pass. With an average of {:.2f}, you are going to have to retake this course.'.format(avg))