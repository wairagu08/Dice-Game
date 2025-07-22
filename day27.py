import os, time
from rich import print
import random

print("\n\t[bold yellow]CHARACTER BUILDER[/bold yellow]\n")
def start():
    legend = input("Name your Legend:\n")
    character = input("Character Type (Human, Elf, Wizard, orc):\n")

    def health():
        sixDice = random.randint(1, 6)
        twelveDice = random.randint(1, 12)
        health = (sixDice * twelveDice)/2 + 10

        print("Health:", health)
    health() 

    def strength():
        sixDice = random.randint(1, 6)
        eightDice = random.randint(1, 8)
        strength = (sixDice * eightDice)/2 + 12
        print("Strength:", strength)
    strength()

    restart = input("Again?: ")
    while restart.lower() == "yes":
        os.system("clear")
        time.sleep(1)
        start()
        continue
    else:
        exit()    
start()