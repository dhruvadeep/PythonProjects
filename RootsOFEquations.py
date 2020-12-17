import math
import cmath

print("===Quadritic Equations===")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

def roots(a, b, c):
    d = (math.pow(b, 2) - (4 * a * c))
    type = "Invalid"
    if d < 0:
        root1 = (-b + cmath.sqrt(d)) / 2 * a
        root2 = (-b - cmath.sqrt(d)) / 2 * a
        type = "Complex"
    elif d >= 0:
        root1 = (-b + cmath.sqrt(d)) / 2 * a
        root2 = (-b - cmath.sqrt(d)) / 2 * a
        if d == 0:
            type = "Equal"
        else:
            type = "Real"
    print("The given equation is a", type)
    print("Roots of this equations are: ")
    print("Root1:", root1)
    print("Root2:",root2)

roots(a,b,c)

