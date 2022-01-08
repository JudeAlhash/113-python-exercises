# EX 24. Write a script that will check if the first word of your answer contains "santo".

city = str(input("In what city were you born?")).lower()
print("santo " in city)
# Only Fails if the city name is just `Santo`

