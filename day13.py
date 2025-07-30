# Exam Grade Calculator
from rich import print
print("\n\t[bold yellow]***Exam Grade Calculator***[/bold yellow]\n")

exam = input("Name of exam: \n")

max_score = int(input("Max. Possible Score: \n"))

your_score = float(input("Your score: \n"))

score = (your_score / max_score) * 100
percent = round(score, 2)
if score >= 90:
    print(f"""excellent
    You got {percent}% which is an A""")
elif score >= 80 and score < 90:
    print(f"""Nice work
    You got {percent}% which is an A-""")
elif score >= 70 and score < 80:
    print(f"""Good
    You got {percent}% which is a B""")
elif score >= 60 and score < 70:
    print(f"""You could do better
    You got {percent}% which is a C""")
elif score >= 50 and score < 60:
    print(f"""You need to work harder
    You got {percent}% which is a D""")
else:
    print(f"""Very poor
    You got {percent,,}% which is a U""")            