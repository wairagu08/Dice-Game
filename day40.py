from rich import print
import time

print("\n\t[bold blue]***CONTACT CARD***[bold blue]")

name = input("Name: ").strip().title()
dob = input("Date of Birth: ")
tel = input("Telephone number: ")
email = input("Email: ")
address = input("Address: ").strip().capitalize()

contact = {"Name": name, "DOB": dob, "Tel": tel, "Email": email, "Address": address}
info = ["Name", "DOB", "Tel", "Email", "Address"]

print()
print("\t[bold green]***Your Contact Info***[/bold green]")
for j in info:
    time.sleep(1)
    print(f"{j}: {contact[j]}")