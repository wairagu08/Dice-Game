from rich import print
print("\n\t[bold yellow]***REPLIT LOGIN SYSTEM***[bold yellow]\n")

def login():
    username = input("What is your username? ")
    password = input("What is your password? ")
    if username == "wairagu" and password == "secure123": 
        print("[italic blue]Welcome to REPLIT[italic blue]")        
    else:
        print("[bold red]Wrong username or password[bold red]")
        
login()