from rich import print
print("\n\t***Math Game!***\n")

multiple = int(input("Name your multiples: "))
score = 0
for i in range(1,11):
    ans = int(input(f"{i} * {multiple} = "))
    if ans == i * multiple:
        print("Great work!\n")
        score += 1
    else:
        print("Nope! The answer was ", i * multiple, "\n")
print(f"Your score is: {score} out of {i}")       

if score == i:
    print("\n\t[bold cyan]You nailed it!!!![bold cyan]")
       