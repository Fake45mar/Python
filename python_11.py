import random as r
class laptop:
    size = 14.1
    price = 200
    proc = 'Intel'
    gpu = 'inside'
    def __init__(self, size, price, proc, gpu):
        self.size = size
        self.price = price
        self.proc = proc
        self.gpu = gpu
size = float(input("Size display "))
price = int(input("Enter price "))
proc = input("Enter proccesor ")
gpu = input("Gpu ")
prestigio = laptop(size,price,proc,gpu)
print(prestigio.size,prestigio.price,prestigio.proc,prestigio.gpu)
