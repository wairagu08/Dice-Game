import os

os.system("clear")
highScore = 0
name = None

file = open("scoreData.txt", "r")
content = file.read().split("\n")
for row in content:
    data = row.split()
    if data != []:
        if int(data[1]) > highScore:
            name = data[0]
            highScore = int(data[1])

print(f"The winner is {name}, with a highscore of {highScore}.")            