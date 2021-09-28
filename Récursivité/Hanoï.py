#!/usr/bin/python
# -*- coding: ISO-8859-15 -*-

def hanoi(n, a=1, b=2, c=3):
    if (n > 0):
        hanoi(n - 1, a, c, b)
        print("Déplace ", a, "sur", c)
        hanoi(n - 1, b, a, c)


hanoi(15)
