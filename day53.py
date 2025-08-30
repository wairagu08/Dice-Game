from rich import print
import time, os, traceback

debugMode = False

inventory = []

try:
    file = open("inventory.txt", "r")
    inventory = eval(file.read())
    file.close()
except:
    if debugMode:
        print(traceback)   

def add():
    print()
    addedItem = input("What do you want to add? ").capitalize()
    inventory.append(adding)
    print("[blue]Added[/blue]")
    time.sleep(1.5)
    os.system("clear")

def view():
    print()
    counted = set(inventory)
    for item in counted:
        print(f"{inventory.count(item)} {item}")
    print()
    time.sleep(1.5)
    os.system("clear")

def remove():
    print()
    removedItem = input("What do you want to remove? ").capitalize()
    if item in inventory:
        inventory.remove(item)
        print("[green]Removed successfully[/green]")
    else:
        print("[bold red]Not found[/bold red]")
    print()
    time.sleep(1)
    os.system("clear")            

while True:
    print("\n\t[bold yellow]INVENTORY[/bold yellow]\n")
    menu = input("1. Add\n2. View\n3. Remove\n4. Exit\n\n> ")
    if menu == "1":
        add()
    elif menu == "2":
        view()
    elif menu == "3":
        remove()
    elif menu == "4":
        exit()    
    else:
        print("[bold red]Invalid option[/bold red]") 
        time.sleep(1)
        os.system("clear")      

    file = open("inventory.txt", "w")
    file.write(str(inventory))
    file.close()     