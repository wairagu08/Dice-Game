# elif
from rich import print

print("""[bold green]MY SYSTEM LOGIN
++++++++++++++++++[/bold green]""")

user = input("Username > ")
password = input("Password > ")

if (user == "francis" or user == "Francis") and password == "fucksociety":
    print(f"""\n\tHello there {user}, what a lovely accent you have,
    you could have charmed your way in here even without
    a password.
    
    Have a great day!""")
elif (user == "wairagu" or user == "Wairagu") and password == "fucksociety":
    print(f"""\n\tHello there {user}, what a lovely accent you have,
    you could have charmed your way in here even without
    a password.
    
    Have a great day!""")
else:
    print("[bold red]ACCESS DENIED[/bold red]")    
        