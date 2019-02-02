print("""Данная программа является калькулятором единиц измирения.
Вы можете выбрать единицу измирения и выбрать во что вам нужно перевести""")
def santi_to_metr(a):
    return a/100
def santi_to_mili(a):
    return a/10
def metr_to_santi(a):
    return a*100
def metr_to_mili(a):
    return a*1000
print("Введите сначало действие, затем введите количество единиц измирения")
print("""Для перевода сантиметров в метры введите santi to meters.
Для перевода сантиметров в милиметры введите santi to mili.
Для перевода метров в сантиметры введите meters to santi.
Для перевода метров в милиметры введите meters to mili.""")
user_input=input()
if user_input == "santi to meters":
    a=float(input())
    print(santi_to_metr(a))
if user_input == "santi to mili":
    a=float(input())
    print(santi_to_mili(a))
if user_input == "meters to santi":
    a=float(input())
    print(metr_to_santi(a))
if user_input == "meters to mili":
    a=float(input())
    print(metr_to_mili(a))


    
    
