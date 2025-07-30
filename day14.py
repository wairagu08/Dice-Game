# Rock Paper Scissors
from getpass import getpass as input
from rich import print

print("\n\t[bold green]***Rock Paper Scissors***[/bold green]\n")
print("""\t[bold red]INSTRUCTIONS[/bold red]
\t\t* Enter r/R for rock.
\t\t* Enter p/P for paper.
\t\t* Enter s/S for scissors.""")


player1 = input("Player 1 > ")
player2 = input("Player 2 > ")

if (player1 == "s" or player1 == "S") and (player2 == "s" or player2 =="S"):
    print("[bold red]No winner, It's a tie![bold red]")
elif (player1 == "r" or player1 == "R") and (player2 == "r" or player2 =="R"):
    print("[bold red]No winner, It's a tie![bold red]")    
elif (player1 == "p" or player1 == "P") and (player2 == "p" or player2 =="P"):
    print("[bold red]No winner, It's a tie![bold red]")
elif player1 == "r" or player1 =="R" and player2 == "s" or player2 == "S":
    print("[bold cyan]Player1 wins![bold cyan]")                
elif player2 == "r" or player2 =="R" and player1 == "s" or player1 == "S":
    print("[bold cyan]Player2 wins![bold cyan]")
elif player1 == "s" or player1 =="S" and player2 == "p" or player2 == "P":
    print("[bold cyan]Player1 wins![bold cyan]")   
elif player2 == "s" or player2 =="S" and player1 == "p" or player1 == "P":
    print("[bold cyan]Player2 wins![bold cyan]")         
elif player1 == "p" or player1 == "P" and player2 == "r" or player2 == "R":
    print("[bold cyan]Player1 wins![bold cyan]")
elif player1 == "r" or player1 == "R" and player2 == "p" or player2 == "P":
    print("[bold cyan]Player2 wins![bold cyan]")    
else:
    print("[bold red]Invalid Syntaxx[/bold red]")           