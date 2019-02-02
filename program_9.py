def foo(l):
    l = list(map(int,l))
    result = 1
    for i in l:
        result = result*i
        print(result)   
l = input(list)
foo(l)
