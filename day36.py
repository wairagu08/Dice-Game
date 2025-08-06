import os, time
from rich import print

names = []

def prettyPrint():
    os.system("clear")
    for i in range(len(names)):
        print(f"{i}. {names[i]}")
    time.sleep(1.5)
    os.system("clear")

while True:
    print("\n\t[bold yellow]***Names List***[/bold yellow]\n")
    first_name = input("First Name: ").strip().capitalize()
    last_name = input("Last Name: ").strip().capitalize()
    full_name = f"{first_name} {last_name}"
    if full_name not in names:
        names.append(full_name)
        prettyPrint()
    else:
        print("[bold red]Error: Duplicate name[/bold red]") 
        time.sleep(1.5)
        prettyPrint()   