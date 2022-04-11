# 010: Write a script that shows how much money she has (in R$) and then convert that value into dollars.
r = float(input(
    'Some sketchy bloke approaches. \n - You got any cash on you, by any chance? I got some dollars i`m tryin to get rid of..'))
d = r / 3.27
print(' - Aight, here`s ya {:.2f} dollars. Gotta run. \n Sketchy guy runs off. Hm.'.format(d))
