def add():
    print("Введите 2 числа")
    a=int(input())
    b=int(input())
    print(a+b)
def diff():
    print("Введите 2 числа")
    a=int(input())
    b=int(input())
    print(a-b)
def div():
    print("Введите 2 числа")
    a=int(input())
    b=int(input())
    print(a/b)
def mul():
    print("Введите 2 числа")
    a=int(input())
    b=int(input())
    print(a*b)
print("""Данная программа выполняет действия простого калькулятора.
Для сложения введите \'sum'.
Для вычитания введите \'diff'.
Для вделения введите \'div'.
Для умножения введите \'mul'.""")
user_input = input()
if user_input == "sum":
    add()
elif user_input == "diff":
    diff()
elif user_input == "div":
    div()
elif user_input == "mul":
    mul()

    
    
