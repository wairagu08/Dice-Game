from rich import print
import os, time, random

characters = {}

characters["Mr spook"] = {"Inteligence": 120, "Speed": 20, "Fun": 90}
characters["David"] = {"Inteligence": 110, "Speed": 40, "Fun": 50}
characters["Superman"] = {"Inteligence": 100, "Speed": 120, "Fun": 20}
characters["Mr robot"] = {"Inteligence": 160, "Speed": 60, "Fun": 100}

while True:
    print("[bold yellow]\n\tTOP TRUMPS\n\nCharacters\n[/bold yellow]")
    for key in characters:
        print(key)
    print()

    player = input("Pick your character\n> ").capitalize()
    if player not in characters:
        print("[bold red]Character not found[/bold red]")
        continue
    comp = random.choice(list(characters.keys()))
    for subkey, subvalue in characters[player].items():
        print(f"{subkey}: {subvalue}")
    print() 
    print(f"> {comp}")   
    for subkey, subvalue in characters[comp].items():
        print(f"{subkey}: {subvalue}")    
    print()        
    stat = input("Choose stats\n> ").capitalize()

    print(f"{player}: {characters[player][stat]}")
    print(f"{comp}: {characters[comp][stat]}")

    if characters[player][stat] > characters[comp][stat]:
        print(f"[bold green]{player} wins![/bold green]")
    elif characters[player][stat] < characters[comp][stat]:
        print(f"[bold green]{comp} wins![/bold green]")
    else:
        print("[bold green]Draw![/bold green]")        

    time.sleep(5)
    os.system("clear")    