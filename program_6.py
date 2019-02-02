def season(i):
    if i <= 3:
        print("winter")
    if i >= 4 and i <= 6:
        print("spring")
    if i >= 7 and i <= 9:
        print("summer")
    if i >= 10 and i <= 12:
        print("autumn")        
i = int(input("Enter a month "))
if i > 12:
    print("You entered variable larger than wanted")
elif i < 13:    
    season(i)
    print("if you want to repeat, enter yes")
    rep = input("enter yes or no")
    if rep == "yes":
        o = int(input("Enter month"))
        season(o)
    elif rep == "no":
       exit 
    else:
        print("Your answer is uncorrect")
            
