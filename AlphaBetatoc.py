#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Esse script organiza uma lista latex (toc) em ordem alfabética.
Ncessário indicar o do arquivo com a lista na variável filename.
'''

filename = 'main.toc'

with open(filename) as f:
    content = f.readlines()

step = 0
Tobesortedlist = []
Finallist = []

while step < len(content):
    if not("subsection" in content[step]):
        for i in sorted(Tobesortedlist):
            Finallist.append(i)
        Tobesortedlist = []
        Finallist.append(content[step])
    else:
        Tobesortedlist.append(content[step])
    step = step + 1

for i in sorted(Tobesortedlist):
            Finallist.append(i)

with open(filename,'w') as f:
    for i in Finallist:
        print(i)
        f.write(i)

#for i in content: 
#    if not("subsection" in i):
#        Sectionlist.append(i)
#
#for i in sorted(content): 
#    if "subsection" in i:
#        Subsectionlist.append(i)
#
#
#
#with open(filename, 'w') as f:
#    for i in content: 
#        if "subsection" in i:
#            f.write(Subsectionlist[Subsection])
#            Subsection = Subsection + 1
#        else:
#            f.write(Sectionlist[Section])
#            Section = Section + 1