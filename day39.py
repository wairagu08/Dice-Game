import random, os, time
from rich import print

listOfWords = ["Apple", "Orange", "Grapes", "pears", "guava","banana" ]
letterPicked = []
lives = 5

word = random.choice(listOfWords)

while True:
    print("\n\t[bold yellow]***HANGMAN GAME***[/bold yellow]")
    letter = input("Choose a letter: ").lower()
    #if letter in letterPicked:
     #   print("[bold red]You've tried that before")
      #  continue
    letterPicked.append(letter)
    if letter in word:
        print("You found a letter!")
        letterPicked.append(letter)
    else:
        print("Letter not in word")
        lives -= 1
        print(f"You have {lives} lives left") 
    allLetters = True
    print()    
    for i in word:
        if i in letterPicked:
            print(i, end="")
        else:
            print("_", end="")
            allLetters = False
    print()            

    if allLetters:
        print(f"You won with {lives} lives left")
        break

    if lives <= 0:
        print("You ran out of lives")    
        break
    else:
        print(f"Only {lives} lives left")    