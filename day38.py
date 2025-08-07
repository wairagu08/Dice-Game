def colorChange(color):
    if color == "r":
        print("\033[31m", end="")
    elif color == " ":
        print("\33[0m", end="")
    elif color == "b":
        print("\33[34m", end="")
    elif color == "y":
        print("\33[33m", end="")
    elif color == "g":
        print("\33[32m", end="")
    elif color == "p":
        print("\33[35m", end="")                        

sentence = input("What sentence do you want to rainbownise?\n")

for letter in sentence:
    colorChange(letter.lower())
    print(letter, end="")
print()    
