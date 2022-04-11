# Create a script that will read a sentence, and then show:
# How many times the letter A appears.
# What's the position of the first letter A.
# What's the position of the last letter A.
string = str(input("What's good dude?").strip()).lower()

print(string.count('a'))
print(int(string.find('a')) + 1)
print(int(string.rfind('a')) + 1)


