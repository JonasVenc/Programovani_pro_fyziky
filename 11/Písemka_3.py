import numpy as np
import math

cisla = []

def zlomek(p, q):
    if p != 0:
        a = math.ceil(q/p)
        cisla.append(a)
        zlomek(a*p-q, q)

zlomek (99, 100)

for i in range(1, len(cisla)):
    cisla[i] = cisla[i] * cisla[i-1]

print (cisla)