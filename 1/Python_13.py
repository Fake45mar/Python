import random as r
i = int(input("Enter quantity "))
def foo(a):
    if a > 0 and a < 11:
        print(a, end = ' ')
    elif a > 11:
        print("This value out of the range")
while i < 1000:
    i+=15
    print('i - ', i)
    a = r.randint(1,11)
    foo(a)
