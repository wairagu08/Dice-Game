# more math
# The answer should be 31,536,000 seconds
from rich import print
print("""\n\t[bold black]***HOW MANY SECONDS ARE THERE IN A YEAR?***
=========================================================[/bold black]\n""")

normal_year = 31+28+31+30+31+30+31+31+30+31+30+31
leap_year = 31+29+31+30+31+30+31+31+30+31+30+31

year = input("Is it leap or normal year?\n")
if year == "leap":
    seconds = int(input("How many seconds are there in a minute?\n"))
    minutes = int(input("How many minutes are there in an hour?\n"))
    hours = int(input("How many hours are there in a day\n"))
    days = leap_year
    months = int(input("How many months are there in a year?\n"))

    total_seconds = seconds * minutes * hours * days
    print(total_seconds)
elif year == "normal":
    seconds = int(input("How many seconds are there in a minute?\n"))
    minutes = int(input("How many minutes are there in an hour?\n"))
    hours = int(input("How many hours are there in a day\n"))
    days = normal_year
    months = int(input("How many months are there in a year?\n"))

    total_seconds = seconds * minutes * hours * days
    print(total_seconds)
else:
    print("Really? What kind of year is this?")       