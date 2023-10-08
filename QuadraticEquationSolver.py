
import math


a = int(input("Entrer le coefficient a de l'équation du second degré : "))
b = int(input("Entrer le coefficient b de l'équation du second degré : "))
c = int(input("Entrer le coefficient c de l'équation du second degré : "))

delta = b ** 2 - 4 * a * c


if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Les solutions sont x1 et x2, donc S =", x1, x2)
elif delta == 0:
    x1 = -b / (2 * a)
    print("La solution unique est x1 =", x1)
else:
    print("Pas de solutions")
