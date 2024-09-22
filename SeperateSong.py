#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Splits up the compiled song files into seperate song files
'''

inputPath = "Kapitel"

outputPath = '../Songs/'

import glob, os
os.chdir(inputPath)
for file in glob.glob("*.tex"):
    #print(file)
    content = []
    with open(file, encoding="utf-8") as f:
        content = f.readlines()
    #print(content)
    section,_ = file.split('.')
    songPath = outputPath + section + "/"
    insideSong = False
    code = []
    songName = ""
    for line in content:
        if "\\begin{SongText}" in line:
            insideSong = True
            song = []
            _,songName = line.split('[')
            songName,_ = songName.split(']')
            songName = "".join(x for x in songName if x.isalnum())
            songName = songName + ".tex"  
        if insideSong == True:
            song.append(line)
        else:
            code.append(line)       
        if "\end{SongText}" in line:
            insideSong = False

            addedSongCodeLine = "\input{Songs/"+section + "/" +songName+"}\n"
            code.append(addedSongCodeLine)

            if not os.path.exists(songPath):
                os.makedirs(songPath)
            with open(songPath+songName,'w+', encoding="utf-8") as s:
                for addedLines in song:
                    print(addedLines)
                    s.write(addedLines)
            s.close()
    f.close()
    with open(file,'w+', encoding="utf-8") as c:
        for addedLines in code:
            print(addedLines)
            c.write(addedLines)
    c.close()
    