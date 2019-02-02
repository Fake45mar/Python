def bank(a,years):
    i = 0
    while i < years:
        i+=1
        print(a+(a/10)*years)
a = int(input("Enter sum"))
years = int(input("Enter period"))
bank(a,years)            
