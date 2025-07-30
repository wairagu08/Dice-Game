from rich import print
import random

print("\n\t[bold white]***Infinity Dice[/bold white]")

def dice(sides):
    sides = int(input("How many sides?: "))
    rolled = random.randint(0,sides)
    print("You rolled", rolled)  
    again = input("Roll again?: ")
    if again.lower() == "yes":
        dice(300)
    else:
        print("Goodbye")
        exit()
dice(300)    