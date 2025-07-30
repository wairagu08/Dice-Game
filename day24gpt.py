from rich import print
import random

print("\n\t[bold white]*** Infinity Dice 🎲 ***[/bold white]")

def dice_game():
    while True:
        try:
            sides = int(input("How many sides?: "))
            if sides < 1:
                print("[red]Please enter a number greater than 0.[/red]")
                continue
        except ValueError:
            print("[red]Please enter a valid number.[/red]")
            continue

        rolled = random.randint(1, sides)  # 1 to sides, not 0
        print(f"[green]You rolled: {rolled}[/green]")

        again = input("Roll again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("[bold blue]Goodbye![/bold blue] 👋")
            break

dice_game()
