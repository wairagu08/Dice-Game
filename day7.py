rom rich import print

print("""\n\n[bold blue]**FAKE FAN FINDER**
----------------------------[/bold blue]""")

movie = input("Are you familiar with the movie Scorpion? ")
if movie == "yes" or movie == "Yes":
    print("Awesome!")
    maincharacter = input("who's the main character then? ")
    if maincharacter == "walter" or maincharacter == "Walter":
        print("That's right!")
        iq = int(input("What is his inteligence quotient measure? "))
        if iq == 197:
            print("[green]You really are a fan. Great.")
        else:
            print("[bold red]I'm disappointed.[/bold red]")    
    else:
        print("[bold red]WRONG![/bold red]")

else:
    print("[bold red] So Booring if you don't know Scorpion")
    