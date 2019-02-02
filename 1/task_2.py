def add(a,b):
    c=a+b
    return c
def diff(a,b):
    c=a-b
    return c
def div(a,b):
    c=a/b
    return c
def mul(a,b):
    c=a*b
    return c
print("""Данная программа выполняет действия простого калькулятора.
Для сложения введите \'sum'.
Для вычитания введите \'diff'.
Для вделения введите \'div'.
Для умножения введите \'mul'.""")
user_input = input()
if user_input == "sum":
    print("Введите 2 числа")
    a=int(input())
    b=int(input())
    print(add(a,b))
elif user_input == "diff":
    print("Введите 2 числа")
    a=int(input())
    b=int(input())
    print(diff(a,b))
elif user_input == "div":
    print("Введите 2 числа")
    a=int(input())
    b=int(input())
    print(div(a,b))
elif user_input == "mul":
    print("Введите 2 числа")
    a=int(input())
    b=int(input())
    print(mul(a,b))

    
    
