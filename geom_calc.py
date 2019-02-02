import math
def geom():
        var_1 = ["Perimetr", "perimetr", "per", "P", "p"]
        var_2 = ["Area", "area"]
        var_3 = ["Diagonal", "diagonal", "Dig", "dig"]
        var_4 = ["Continue", "continue", "again", "Again", "", " "]
        def square(a):
                ch = input("Switch the action : perimetr, area, diag - ")
                def per(a):
                        P = 4*a
                        print("Perimetr equal ",P)
                        print("If do you want, you can calculate again, press or \'again or continue' or free space")
                        ag = input()
                        if ag in var_4:
                                geom()
                        else:
                                quit()
                def area(a):
                        S = pow(a,2)
                        print("Area of square equal ",S)
                        print("If do you want, you can calculate again, press or \'again or continue' or free space")
                        ag = input()
                        if ag in var_4:
                                geom()
                def dig(a):
                        D = a*math.sqrt(2)
                        print("Main diagonal equal",D)
                        print("If do you want, you can calculate again, press or \'again or continue' or free space")
                        ag = input()
                        if ag in var_4:
                                geom()
                        else:
                                quit()
                if ch in var_1:
                        per(a)
                elif ch in var_2:
                	area(a)
                elif ch in var_3:
                        dig(a)
                else:
                        print("Your input incorrect, please, try again")
                        square(a)
        def rect(a,b):
                ch = input("Switch the action : perimetr, area, diag - ")
                var_1 = ["Perimetr", "perimetr", "per", "P", "p"]
                var_2 = ["Area", "area"]
                var_3 = ["Diagonal", "diagonal", "Dig", "dig"]
                def per(a,b):
                        P = 2*a + 2*b
                        print("Perimetr equal",P)
                        print("If do you want, you can calculate again, press or \'again or continue' or free space")
                        ag = input()
                        if ag in var_4:
                                geom()
                        else:
                                quit()
                def area(a,b):
                        S = a*b
                        print("Area equal ",S)
                        print("If do you want, you can calculate again, press or \'again or continue' or free space")
                        ag = input()
                        if ag in var_4:
                                geom()
                        else:
                                quit()
                def dig(a,b):
                        D = math.sqrt(math.pow(a,2)+math.pow(b,2))
                        print("Main diagonal equal ",D)
                        print("If do you want, you can calculate again, press or \'again or continue' or free space")
                        ag = input()
                        if ag in var_4:
                                geom()
                        else:
                                quit()
                if ch in var_1:
                        per(a)
                elif ch in var_2:
                        area(a)
                elif ch in var_3:
                        dig(a,b)
                else:
                        print("Your input incorrect, please, try again")
                        rect(a,b)
        def tr(a,b,c):
                ch = input("Switch the action : perimetr, area - ")
                var_1 = ["Perimetr", "perimetr", "per", "P", "p"]
                var_2 = ["Area", "area"]
                def per(a,b,c):
                        P = a+b+c
                        print("Perimetr equal ",P)
                        print("If do you want, you can calculate again, press or \'again or continue' or free space")
                        ag = input()
                        if ag in var_4:
                                geom()
                        else:
                                quit()
                def area(a,b,c):
                        if a == b == c:
                                S = (math.pow(a,2)*math.sqrt(3))/4
                                print("Area equal",S)
                                print("If do you want, you can calculate again, press or \'again or continue' or free space")
                                ag = input()
                                if ag in var_4:
                                        geom()
                        elif (a==b) or (a==c) or (b==c):
                                H = math.sqrt(math.pow(b,2)-math.pow(c,2))
                                S = 1/2*a*H
                                print("High is",H,"\nArea equal",S)
                                print("If do you want, you can calculate again, press or \'again or continue' or free space")
                                ag = input()
                                if ag in var_4:
                                        geom()
                                else:
                                        quit()

                        else:
                                p = (a+b+c)/2
                                S = math.sqrt(p*(p-a)*(p-b)*(p-c))
                                print("Half perimetrr equal ",p,"\nArea equal ",S)
                                print("If do you want, you can calculate again, press or \'again or continue' or free space")
                                ag = input()
                                if ag in var_4:
                                        geom()
                                else:
                                        quit()
                if ch in var_1:
                        per(a,b,c)
                elif ch in var_2:
                        area(a,b,c)
                else:
                        print("Your input incorrect, please, try again")
                        tr(a,b,c)
        def par(a,b,c):
                ch = input("Enter the action: perimetr, area, diagonal. ")
                var_1 = ["Perimetr", "perimetr", "per", "P", "p"]
                var_2 = ["Area", "area"]
                var_3 = ["Diagonal", "diagonal", "Dig", "dig"]
                def per(a,b):
                        P = 2*a + 2*b
                        print("Perimetr equal ",P)
                        print("If do you want, you can calculate again, press or \'again or continue' or free space")
                        ag = input()
                        if ag in var_4:
                                geom()
                        else:
                                quit()
                def area(a,b,c):
                        H = math.sin(c)*b
                        S = 1/2*a*H
                        print("High equal ",H,"\nArea equal ",S)
                        print("If do you want, you can calculate again, press or \'again or continue' or free space")
                        ag = input()
                        if ag in var_4:
                                geom()
                        else:
                                quit()
                def dig(a,b,c):
                        D = math.sqrt(math.pow(a,2) + math.pow(b,2) - 2*a*b*math.cos(c))
                        print("Main diagonal equal ",D)
                        print("If do you want, you can calculate again, press or \'again or continue' or free space")
                        ag = input()
                        if ag in var_4:
                                geom()
                        else:
                                quit()
                if ch in var_1:
                        per(a,b,c)
                elif ch in var_2:
                        area(a,b,c)
                elif ch in var_3:
                        dig(a,b,c)
                else:
                        print("Your input incorrect, please, try again")
                        per(a,b,c)  
        print("""Hello! This program is geometric calculator and it ables calculate area, perimetr
and etc.
In inception, you have to enter few variable and after you can see magic C= .""")
        try:
                a = int(input("Enter the variable - "))
                b = int(input("Enter the variable - "))
                c = int(input("Enter the variable - "))
        except ValueError:
                print("ERROR 404! You did not enter  values, try again\n")
                geom()
        var = ["Square", "square", "Sq", "sq"]
        vr = ["Rectangle", "rectangle", "rect", "Rect"]
        v = ["Triangle", "triangle", "tri", "Tri"]
        ch = input("Enter the figure: square, rectangle, triangle. ")
        if ch in var:
                square(a)
        elif ch in vr:
                rect(a,b)
        elif ch in v:
                tr(a,b,c)
        elif ch == "end":
                quit()
        else:
                print("You entered incorrect figure, try again")
                geom()
geom()

