import random, time, os
from rich import print

print("\n\t[bold yellow]David's Nan's Bingo Card Generator[/bold yellow]")

bingo = []

def ran():
    number = random.randint(1,99)
    return number

def prettyPrint():
    for row in bingo:
        for item in row:
            print(f"{item:^10}", end=" | ") 
        print()
        print("------------------------------------------")
    print()        

def create_card():
    global bingo
    numbers = []
    for i in range(8):
        num = ran()
        while num in numbers:
            num = ran()
        numbers.append(ran()) 

    numbers.sort()

    bingo = [[numbers[0], numbers[1], numbers[2]],
            [numbers[3], "Bingo", numbers[4]],
            [numbers[5], numbers[6], numbers[7]]]


create_card()

while True:
    prettyPrint()
    num = int(input("Enter number: "))
    for row in range(len(bingo)):
        for item in range(len(bingo[row])):
            if bingo[row][item] == num:
                bingo[row][item] = "X"
    exes = 0
    for row in bingo:
        for item in row:
            if item == "X":            
                exes += 1
    if exes == 8:
        print("[bold blue]You have won![/bold blue]") 
        break           

    time.sleep(1)
    os.system("clear")    