from rich import print
import time

print("\n\t[bold green]-_-WEBSITE INFO-_-[/bold green]")

web_info = {"name": None, "url": None, "Desc": None, "Rating": None}

for name, value in web_info.items():
    web_info[name] = input(f"{name}: ")
print()

for name, value in web_info.items():
    time.sleep(1.5)
    print(f"[bold yellow]{name}: {value}[/bold yellow]")