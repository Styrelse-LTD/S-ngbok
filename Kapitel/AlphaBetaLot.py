#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Esse script organiza uma lista latex (toc) em ordem alfabética.
Ncessário indicar o do arquivo com a lista na variável filename.
'''

filename = 'main.toc'

with open(filename) as f:
    content = f.readlines()

with open(filename, 'w') as f:
    for i in sorted(content):
        f.write(i)