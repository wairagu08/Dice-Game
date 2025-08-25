from rich import print
import os, time

todo = [["Name", "Due", "Priority"]]

def add():
    time.sleep(1)
    os.system("clear")
    name = input("What to add: ")
    due = input("When is it due? ")
    priority = input("Priority(high, medium, low): ").lower()
    row = [name, due, priority]
    todo.append(row)
    print("Added")
    time.sleep(1)
    os.system("clear")

def view():
    time.sleep(1)
    os.system("clear")
    check = int(input("1. View all\n2. Priority\n>"))
    if check == 1:
        for row in todo:
            for item in row:
                print(f"{item:^10}", end=" | ")
            print()
        print()
        time.sleep(2)
        os.system("clear")         
    else:
        priority = input("Enter priority: ").lower()
        for row in todo:
            if priority in row:
                for item in row:
                    print(f"{item:^10}", end=" | ") 
                print()
        print()
        time.sleep(2)
        os.system("clear") 

def edit():
    time.sleep(1)
    os.system("clear")
    find = input("What do you want to edit? ").lower()
    found = False
    for row in todo:
        if find in row:
            found = True
            for item in row:
                    todo.remove(row)
                    print("[green]Editing.....[/green]")
                    name = input("New name: ")
                    due = input("New due date? ")
                    priority = input("New priority(high, medium, low): ").lower()
                    row = [name, due, priority]
                    todo.append(row)
                    print("[green]Edited successfully[/green]")
                    return
        time.sleep(1)
        os.system("clear")
    if not found:
        print("[bold red]Couldn't find that[/bold red]")
        time.sleep(2)
        os.system("clear")

def remove():
    find = input("What do you want to remove? ").lower()
    found = False
    for row in todo:
        if find in row:
            found = True
            print("[green]Removing......")
            todo.remove(row)
            print("[green]Removed successfully[/green]")
            time.sleep(1)
            os.system("clear")
    if not found:
        print("[bold red]Couldn't find that[/bold red]")
        time.sleep(2)
        os.system("clear")                        

while True:
    print("\n\t[bold yellow]TODO MANAGEMENT SYSTEM[/bold yellow]\n")
    menu = int(input("1. Add\n2. View\n3. Edit\n4. Remove\n\n>"))
    if menu == 1:
        add()
    elif menu == 2:
        view()
    elif menu == 3:
        edit()
    else:
        remove()        