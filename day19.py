from rich import print

print("\n[bold green]Loan Calculator[bold green]\n")
initial_loan = int(input("How much is your loan? \n"))
loan = initial_loan
interest = int(input("Interest: \n"))
print(f"ksh.{loan} over 10 years at {interest}% annual interest rate")

for years in range(10):
    years += 1
    loan *= (interest + 100) / 100
    amnt2 = round(loan, 2)
    print(f"Year {years} is ksh.{amnt2}")
print("Your total interest is ", amnt2 - initial_loan)
