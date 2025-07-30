import os, time
from rich import print

ToDo_list = []

def printList():
    print()
    for item in ToDo_list:
        print(item)
    print()

print("\n\t[bold yellow]***ToDo List Manager***[/bold yellow]\n")

while True:
    action = input("Do you want to view, add or remove the todo list? ")
    if action == "view":
        printList()

    elif action == "add":
        item = input("What do you want to add? ")
        ToDo_list.append(item)
        printList()
        time.sleep(1)
        os.system("clear")
    elif action == "remove":
        item = input("What item do you want to remove? ")
        if item in ToDo_list: 
            ToDo_list.remove(item)
            printList()

        else:
            print(f"{item} not in the list")
            printList()
