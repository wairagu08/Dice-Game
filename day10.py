# A bit of math
from rich import print

print("""[bold green]    ***TIP CALCULATOR***
-_-_-_-_-_-_-_-_-_-_-_-_-_-_[/bold green]""")

bill = float(input("How much did you spend?\n"))
tip = float(input("What percentage do you want to tip?\n"))
members = int(input("How many people are in you group?\n"))

tip = (tip / 100) * bill
total = bill + tip
share = total / members

print(f"Total = ${total}")
print(f"You each owe ${share}")