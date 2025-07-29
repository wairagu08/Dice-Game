#!/bin/python3

def color(color):
    if color == "red":
        return ("\033[31m")
    elif color == "white":
        return ("\033[0m")
    elif color == "blue":
        return ("\033[34m")
    elif color == "green":
        return ("\033[32m")
    elif color == "yellow":
        return ("\033[33m")
    elif color == "purple":
        return ("\033[35m")

title = f"{color('red')}={color('white')}={color('blue')}= {color('yellow')}Music App {color('blue')}={color('white')}={color('red')}="
print(f"                {title:^35}\n")
print(f"🔥⏯️\t{color('white')}Radio Gaga")
print(f"\t{color('yellow')}Queen\n\n")

prev = 'PREV⏮️'
next = "NEXT⏭️"
pause = "PAUSE⏸️"

print(f"{color('white')}{prev:<30}")
print(f"{color('green')}{next:^30}")
print(f"{color('purple')}{pause:>30}\n\n\n")

title = "WELCOME TO"
print(f"{color('white')}{title:^35}")
title = "--     ARMBOOK     --"
print(f"{color('blue')}{title:^35}")
text = "Definitely not a rip off of"
print(f"{color('yellow')}{text:^35}")
text = "a certain other social"
print(f"{color('yellow')}{text:^35}")
text = "networking site."
print(f"{color('yellow')}{text:^35}\n")
text = "Honest."
print(f"{color('red')}{text:^35}\n")

user = input(f"{color('white'):^18}Username: ")
password = input(f"{color('white'):^18}Password: ")