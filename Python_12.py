class robot:
    def __init__(self,switch):
        self.switch = switch
        if switch == 1:
            case = int(input("Switch a product"))
            if case == 1:
                print("Your candy is waiting for you!")
            elif case == 2:
                print("Your cake is waiting for you!")
            elif case == 3:
                print("Your chips is waiting for you")
        elif switch == 2:
            case = int(input("Switch a product"))
            if case == 1:
                print("Your coca-cola is waiting for you!")
            elif case == 2:
                print("Your fanta is waiting for you!")
            elif case == 3:
                print("Your sprite is waiting for you")
            else:
                print("Repeating")
                switch = int(input("Choose the option"))
                r = robot(switch)
def swit():                
    switch = int(input("Choose the option"))
    if switch == 1 or 2:
        r = robot(switch)
    else:
        #swit()
        print("You choosen incorrect button")
swit()
