from rich import print

print("\n[bold blue]List Generator[bold blue]\n")

start = int(input("Start at: \n"))
end = int(input("End before: \n"))
increment = int(input("Increment by: \n"))

for i in range(start, end, increment):
    print("\n", i)