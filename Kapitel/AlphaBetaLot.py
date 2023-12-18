f = open("main.lot", "r")

songs = []
Name = ""
for x in f.read():
    if x == '%':
        Name.removeprefix('\\contentsline {table}{')
        songs.append(Name)
        Name = ""
    else:
        Name = Name + x
songs.sort

print(songs)
