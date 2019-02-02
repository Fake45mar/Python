def is_year_leap(year):
    if year % 4 == 0:
        print("This year is leap")
    else:
        print("This is not leap year")
year = int(input("Write year"))
is_year_leap(year)
