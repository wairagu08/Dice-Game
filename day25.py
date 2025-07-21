import random
from rich import print

print("\n\t[bold green]CHARACTER STAT GENERATOR[/bold green]\n")

warrior = ["Agnes", "Ian", "Penelope"]
print(f"Warriors: {warrior}")

def warriors():
    num = random.randint(1, 3)
    if num == 1:
        print(f"Your warrior is warrior number {num} \"{warrior[0]}\"")
        return num
    elif num == 2:
        print(f"Your warrior is warrior number {num} \"{warrior[1]}\"")
        return num
    else:
        print(f"Your warrior is warrior number {num} \"{warrior[2]}\"")
        return num
warriors()        
    
def warrior_health(dice1, dice2):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1,8)
    health = dice1 * dice2
    return health
d1 = input("Roll six-sided dice: ") 
d2 = input("Roll eight-sided dice: ")   
power = warrior_health(d1, d2)
print(f"Their health is {power}hp")    

