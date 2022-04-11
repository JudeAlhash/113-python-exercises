# EX 101 : Create a function called vote() that will receive someone's birth year, and determine if they are eligible
# to vote or not.

def vote(y):
    """Using your birth year as an argument, this code will determine whether you can vote or not."""
    from datetime import datetime
    age = datetime.now().year - y
    if age >= 16:
        return 'Eligible to vote!'
    else:
        return 'Cannot vote yet.'


print(vote(int(input('What is your year of birth?'))))
