from rich import print
import os, time, random

def add():
    time.sleep(1)
    os.system("clear")
    file = open("ideas.txt", "a+")
    ideas = input("Idea > ")
    file.write(f"{ideas}\n")
    file.close()
    time.sleep(1)
    os.system("clear")

def show():
    time.sleep(1)
    os.system("clear")
    file = open("ideas.txt", "r")
    ideas = file.read().split("\n")
    file.close()
    idea = random.choice(ideas)
    print(idea)
    time.sleep(3)
    os.system("clear")

while True:
    print("\n\t[bold yellow]IDEAS[/bold yellow]\n")
    menu = int(input("1: Add an idea\n2: Load up a random idea\n3: Exit\n\n> "))
    if menu == 1:
        add()
    elif menu == 2:
        show()
    elif menu == 3:
        exit()
    else:
        print("[bold red]Invalid option")
        continue        