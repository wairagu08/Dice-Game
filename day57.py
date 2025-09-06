# Factorial tree
from rich import print

def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("\n\t[bold yellow]FACTORIAL TREE[/bold yellow]\n")
print(factorial(10))            