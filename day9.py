from rich import print

print("""\n\n[bold green]\t***GENERATION IDENTIFIER***
=======================================""")

birthday = int(input("Which year were you born? \n"))

if birthday <= 1900 and birthday >= 1883:
    print("Hah! You are a [bold cyan]Lost Generation.[/bold cyan]")
elif birthday <= 1927 and birthday >= 1901:
    print("Hah! You are a [bold cyan]Greatest Generation.[/bold cyan]")
elif birthday <= 1945 and birthday >= 1928:
    print("Hah! You are a [bold cyan]Silent Generation.[/bold cyan]")
elif birthday <= 1964 and birthday >= 1946:
    print("Hah! You are a [bold cyan]Baby Boomer.[/bold cyan]")
elif birthday <= 1980 and birthday >= 1965:
    print("Hah! You are a [bold cyan]Generation X.[/bold cyan]")  
elif birthday <= 1996 and birthday >= 1981:
    print("Hah! You are a [bold cyan]Millennial.[/bold cyan]")          
elif birthday <= 2012 and birthday >= 1997:
    print("Hah! You are a [bold cyan]Gen Z.[/bold cyan]")
elif birthday > 2012:
    print("Hah! You are a [bold cyan]Gen Alpha.[/bold cyan]")
else:
    print("[bold red]Unknown Generation[/bold red]")        