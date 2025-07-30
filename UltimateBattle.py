import os, random, time
from rich import print

def rollDice(side):
    result = random.randint(1, side)
    return result

def health():
    healthStat = ((rollDice(6)*rollDice(12))/2) + 10
    return healthStat

def strength():
    strengthStat = ((rollDice(6)*rollDice(8))/2)+12
    return strengthStat

print("\n\tBATTLE TIME\n")
char1 = input("Name your Legend:\n")
c1_type = input("Character type (Human, Elf, Wizard, orc):\n")
print(char1)
c1Health = health()
c1Strength = strength()
print("Health:", c1Health)
print("Strength:", c1Strength) 
print("\n\t[bold black]Who are they battling?") 

char2 = input("Name your Legend:\n")
c2_type = input("Character type (Human, Elf, Wizard, orc):\n")
print(char2)
c2Health = health()
c2Strength = strength()
print("Health:", c2Health)
print("Strength:", c2Strength)  

round = 1
winner = None

while True:
    time.sleep(1)
    os.system("clear")
    print("\n\tBATTLE TIME\n")
    print("\t[bold black]The battle begins[/bold black]")

    c1Dice = rollDice(6)
    c2Dice = rollDice(6)

    difference = abs(c1Strength - c2Strength) + 1
    if c1Dice > c2Dice:
        c2Health -= difference
        if round == 1:
            print(char1, "wins the first blow")
        else:
            print(char1, "wins round", round)
    elif c2Dice > c1Dice:   
        c1Health -= difference
        if round == 1:
            print(char2, "wins the blow")
        else:
            print(char2, "wins round", round)  
    else:
        print("Their swords clash and they draw round", round)

    print(char1)      
    print("Health:", c1Health)
    print()
    print(char2)
    print("Health", c2Health)          
    print()   

    if c1Health <= 0:
        print(char1, "has died!")
        winner = char2
        break
    elif c2Health <= 0:
        print(char2, "has died!")
        winner = char1
        break    
    else:
        print("And both are standing for the next round")
        round +=1

time.sleep(1)
os.system("clear")
print("\tBATTLE TIME\n")
print(winner, "has won in", round, "rounds")
