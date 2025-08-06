import os, time
from rich import print

todo_list = []

def prettyPrint():
    os.system("clear")
    for index in range(len(todo_list)):
        print(f"{index} : {todo_list[index]}")
    time.sleep(1.5)
    os.system("clear")

while True:
    print("\n\t[bold yellow]ToDo List Manager 2[/bold yellow]\n")
    option = input("Do you want to view, add, remove or clear the todo list?\n")
    if option ==  "view":
        prettyPrint()
    elif option == "add":
        item = input("What do you want to add?\n>")
        if item in todo_list:
            print("[bold green]Already in the list[/bold green]")
            time.sleep(1.5)
            os.system("clear")
        else:    
            todo_list.append(item)
            os.system("clear")
    elif option == "remove":
        item = input("What do you want to remove?\n>")
        todo_list.remove(item)
        prettyPrint()
    elif option == "clear":
        todo_list.clear()
        prettyPrint()                