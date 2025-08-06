import os, time
from rich import print

listOfEmails = []

def prettyPrint():
    os.system("clear")
    print("ListOfEmails\n")
    for index in range(len(listOfEmails)):
        print(f"{index} : {listOfEmails[index]}")
    time.sleep(2)    
    os.system("clear")

while True:
    print("\n\t[bold yellow]SPAMMING INC.[/bold yellow]\n")
    menu = input("1: Add email\n2: remove email\n3: Show email\n4: Get SPAMMING\n>")
    if menu == "1":
        email = input("\nEmail > ")
        listOfEmails.append(email)
        os.system("clear")
    elif menu == "2":
        email = input("\nEmail > ")
        if email in listOfEmails:
            listOfEmails.remove(email)
            prettyPrint()
        else:
            print("[bold red]Email not found[/bold red]")
        time.sleep(2)        
        os.system("clear")    

    elif menu == "3":
        prettyPrint()
    elif menu == "4":
        for i in range(min(3, len(listOfEmails))):
            print(f"""Email {i}
            
            Dear {listOfEmails[i]}
            It has come to our attention that you're missing out on
            the amazing Replit 100 days of code. We insist you do it
            right away. If you don't we will pass on your email
            address to every spammer we've ever encountered and also
            sign you up to the My Little Pony newsletter, because
            that's neat. We might just do that anyway.
            
            Love and hugs,
            Luise spammington III""")
            time.sleep(1.5)