# While loop
from rich import print
print("""\n\t\t[bold green]***Animals***[bold green]
[italic blue]> Cow
> Sheep
> Cat[italic blue]""")

animal = input("\nwhat animal do you want? : ")

if animal == "cow":
    print("[bold black]A cow goes moo.[bold black]")
elif animal == "sheep":
    print("[bold black]A sheep goes mee.[bold black]")
elif animal == "cat":
    print("[bold black]A cat goes meow.[bold black]")
else:
    while True:
        exit = input("Do you want to exit? ")
        if exit == "yes":
            break