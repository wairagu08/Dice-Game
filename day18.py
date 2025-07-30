from rich import print

print("\n\t[bold magenta]One-Hunderd-To-One[bold magenta]")
print("\n[italic cyan]In ths game you're going to guess a number between 1 and 100. Enjoy[italic cyan]")
num = 44
number_of_guesses = 0
guess = ""
while guess != num:
    guess = int(input("What is your guess? \n"))

    if guess < 38 and guess > 0:
        print("Too low\n")
        number_of_guesses += 1
    elif guess > 50 and guess <= 100:
        print("Too high\n")
        number_of_guesses += 1
    elif guess >= 38 and guess < num:
        print("Slightly low\n")
        number_of_guesses += 1
    elif guess <= 50 and guess > num:
        print("Slightly high\n")
        number_of_guesses += 1
        continue
    elif guess <= 0 or guess > 100:
        print("[bold red]Invalid[bold red]")
        exit()
    else:
        number_of_guesses += 1
        print(f"""Correct
It took you {number_of_guesses} guesses to get it correct!""")
        break        
