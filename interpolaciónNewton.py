from math import *
from pprint import pprint

def NewtonPol(datos):
    n = len(datos) - 1
    F = [[0 for x in datos] for x in datos]

    for i, p in enumerate(datos):
        F[i][0] = p[1]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            F[i][j] = (F[i][j-1] - F[i-1][j-1]) / (datos[i][0] - datos[i-j][0])

    def L(k, x):
        out = 1.0
        for i, p in enumerate(datos):
            if i <= k:
                out *= (x - p[0])
        return out

    def P(x):
        newt = 0.0
        for i in range(1, n + 1):
            newt += F[i][i] * L(i - 1, x)

        return newt + F[0][0]

    return F, P
#datost = [(3.0, 2310), (5.0, 3090), (7.0, 3940), (20.0, 8000)]
datost = [(-1.0, 0), (3.0, -1.0), (5.0,-3.0), (7.0, 3.0),(9.0,0)]
F, P = NewtonPol(datost)
print("\n Tabla de diferencias divididas:")
pprint(F)

print("\n Evaluar el polinomio en x=10")
print(P(7.2))
