import time, os

print("\n\tMokeBeast")

specs = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}
beast_type = ["water", "fire", "air","earth"]
print("\nBeast Types:")

for i in beast_type:
    print(f"\t{i}") 
print()    

for name in specs:
    specs[name] = input(f"{name}: ").strip().lower()

if specs["Type"] == "water":
    print("\33[34m", end="")
elif specs["Type"] == "earth":
    print("\33[32m", end="")
elif specs["Type"] == "fire":
    print("\33[31m", end="")
elif specs["Type"] == "air":
    print("\33[37", end="")
else:
    print("\33[33", end="")
print()

os.system("clear")
for name, value in specs.items():
    time.sleep(1)
    print(f"{name}: {value}")
