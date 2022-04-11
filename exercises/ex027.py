# Ex27 Write a script that will read a full name, and tell you the First and Last names given.

name = str(input("Type in your full name.")).strip()
split = name.split()
X = len(split)
print(split[X-1])
print(split[0])

