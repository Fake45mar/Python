from math import sqrt
def square(a):
    b = (a+a,a*a,a*sqrt(2))
    return b
a = int(input("Vvedite a"))
print(square(a))
