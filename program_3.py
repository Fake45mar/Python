def foo(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + foo(array[1:])

array = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
for i, elem in enumerate(array):
    array[i] = int(elem)
print(foo(array)) 
