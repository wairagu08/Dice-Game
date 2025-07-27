def coloredText(color, text):
    if color == "red":
        print("\33[31m", text, sep="", end="")
    elif color == "blue":
        print("\33[34m", text, sep="", end="")
    elif color == "green":
        print("\33[32m", text, sep="", end="")    
    else:
        print("\33[0m", text, sep="", end="")
print("Super Subroutine\n")
print("With my ", end="")    
coloredText("green", "new program ")
coloredText("none","I can just call red('and') ")
coloredText("red", "and ")
coloredText("none", "That word will appear in the color I set it to.\n")            
coloredText("onn", "With no ")
coloredText("blue", "weird gaps.\n")  
coloredText("green", "Epic.")  