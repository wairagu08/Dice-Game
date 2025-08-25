from rich import print
import time, os

beast = {}

def prettyPrint():
    print()
    for key, value in beast.items():
        print(f"{key:^10}", end=" | ")
        for subkey, subvalue in value.items():
            print(f"{subvalue:^10}", end=" | ")
        print()  

while True:
    print("\n\t[bold yellow]MokeBeasts Full-on MokeDex\
    [/bold yellow]\n")
    print("[yellow]Add Your Beast[/yellow]")
    name = input("Name > ")
    beastType = input("Type > ")
    hp = input("HP > ")
    mp = input("MP > ")

    beast[name] = {"Type": beastType, 
                    "HP": hp,
                    "MP": mp}

    prettyPrint()
    time.sleep(2)
    os.system("clear")