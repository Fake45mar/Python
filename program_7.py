def bank(a,years):
    while years > 0:
        b = a+(a//10)*years
        years -=1
        print(b)
a = int(input("Enter sum"))
years = int(input("Enter period(years)"))
bank(a,years)            
