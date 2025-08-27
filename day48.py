from rich import print
import os, time

scoreTable = open("scoreData.txt", "a+")

while True:
    print("\n[bold yellow]HIGH SCORE TABLE[/bold  yellow]\n")
    initials = input("INITIALS > ")
    score = int(input("SCORE > "))
    print("\n[blue]ADDED[blue]")
    time.sleep(3)
    os.system("clear")
    scoreTable.write(f"{initials} {score}\n")
    print()

    add = input("Continue or exit?\n> ")
    if add.lower()[0] == "c":
        continue
    elif add.lower()[0] == "e":
        exit()

    scoretable.close()        