from getpass import getpass as input
from rich import print

print("\n\t[bold green]***Rock Paper Scissors***[/bold green]\n")
print("""\t[bold red]INSTRUCTIONS[/bold red]
\t\t* Enter r/R for rock.
\t\t* Enter p/P for paper.
\t\t* Enter s/S for scissors.""")

print("[bold green]ROUND 1[bold green]")
player1_score = 0
player2_score = 0

while player1_score < 3 and player2_score < 3:
    player1 = input("Player 1 > ")
    player2 = input("Player 2 > ")

    if player1.lower() == player2.lower():
        print("[bold red]No winner, It's a tie![bold red]")
        print(f"Player1 score: {player1_score}\tPlayer2_score: {player2_score}")
    elif player1 == "r" or player1 =="R" and player2 == "s" or player2 == "S":
        print("[bold cyan]Player1 wins![bold cyan]")
        player1_score += 1
        print(f"Player1 score: {player1_score}\tPlayer2_score: {player2_score}")                
    elif player2 == "r" or player2 =="R" and player1 == "s" or player1 == "S":
        print("[bold cyan]Player2 wins![bold cyan]")
        player2_score += 1
        print(f"Player1 score: {player1_score}\tPlayer2_score: {player2_score}")
    elif player1 == "s" or player1 =="S" and player2 == "p" or player2 == "P":
        print("[bold cyan]Player1 wins![bold cyan]")
        player1_score += 1
        print(f"Player1 score: {player1_score}\tPlayer2_score: {player2_score}")   
    elif player2 == "s" or player2 =="S" and player1 == "p" or player1 == "P":
        print("[bold cyan]Player2 wins![bold cyan]")
        player2_score += 1
        print(f"Player1 score: {player1_score}\tPlayer2_score: {player2_score}")         
    elif player1 == "p" or player1 == "P" and player2 == "r" or player2 == "R":
        print("[bold cyan]Player1 wins![bold cyan]")
        player1_score += 1
        print(f"Player1 score: {player1_score}\tPlayer2_score: {player2_score}")
    elif player1 == "r" or player1 == "R" and player2 == "p" or player2 == "P":
        print("[bold cyan]Player2 wins![bold cyan]")
        player2_score += 1
        print(f"Player1 score: {player1_score}\tPlayer2_score: {player2_score}")    
    else:
        print("[bold red]Invalid Syntaxx[/bold red]")  
    continue
if player1_score > player2_score:
    print("[bold cyan]Player1 wins the round![bold cyan]")
else:
    print("[bold cyan]Player2 wins the round![bold cyan]")    