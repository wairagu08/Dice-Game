from rich import print
import os, time, traceback

debugMode = False

orders = [["Name", "Topping", "Size", "Quantity", "Total"]]

try:
    file = open("theLurk.txt", "r")
    orders = eval(file.read())
    file.close()
except:
    if debugMode:
        print(traceback)

def prettyPrint():
    time.sleep(1)
    os.system("clear")
    for row in orders:
        for item in row:
            print(f"{item:^10}", end=" | ")
        print()
    print()        

while True:
    print("\n\t[bold yellow]The Lurk Pizza[/bold yellow]\n")
    name = input("what's your name? ")
    topping = input("What topping? ")
    size = input("what size? ")
    quantity = int(input("How many? "))
    price = 12.5
    total = price * quantity
    order = [name, topping, size, quantity, total]
    orders.append(order)
    time.sleep(2)
    os.system("clear")
    prettyPrint()

    file = open("theLurk.txt", "w")
    file.write(str(orders))
    file.close()