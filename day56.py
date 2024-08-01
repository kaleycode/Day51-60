import csv, os

print("⭐️ Day 56 Challenge ⭐️")
print()
with open("100MostStreamedSongs.csv") as file: 
  reader = csv.DictReader(file) 
  for row in reader:
    dir = os.listdir()
    artist = row["Artist(s)"]
    song = row["Song"]
    print(artist)
    print(song)
    print()
    if artist not in dir:
      os.mkdir(artist)
    path = os.path.join(f"{artist}/", song)
    f = open(path, "w")
    f.close()
