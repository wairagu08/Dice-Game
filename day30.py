# f-string for concatenation and alignment
from rich import print

print("\n\t[bold black]30 Days Down - what did you think?[/bold black]\n")

for i in range(1, 30):
    day = input(f"Day {i}:\n")
    print(f"[italic cyan]\tYou thought Day {i} was\n\t{day}[/italic cyan]")