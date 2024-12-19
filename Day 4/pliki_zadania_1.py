#!/usr/bin/env python
#-*- coding: utf8 -*-

# działania z plikami

with open('test2.log', "w", encoding='utf-8') as fh:
    fh.write("Powitanie\n")

with open('test2.log', "a", encoding='utf-8') as fh:
    fh.write("Kolejna wiadomość\n")
    fh.write("Druga wiadomość\n")
    fh.write("Trzecia wiadomość\n")
    fh.write("Czwarta wiadomość\n")
    fh.write("Piąta wiadomość\n")
    fh.write("Szósta wiadomość\n")

with open('test2.log', "r", encoding='utf-8') as fh:
    lines = fh.read()

print(lines)



