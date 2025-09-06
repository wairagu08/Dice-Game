import os, csv

with open("Top 100 most Streamed - Sheet1.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dir = os.listdir()
        artist = row["artist"].title()

        if artist not in dir:
            os.mkdir(artist)
        song = row["title"]
        path = os.path.join(f"{artist}/", song)

        f = open(path, "w")
        f.close()