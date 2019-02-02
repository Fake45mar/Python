def foo(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0]+foo(array[1:])

array = list(input("vvedi massiv"))
array = [int(elem) for elem in array]
print (foo(array))
