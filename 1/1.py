while True:
    print("Options:")
    print("Enter \'add' to add two variables")
    print("Enter\'subtract' to subtract two variables")
    print("Enter\'multiply' to multiply two variables")
    print("Enter\'divide' to divide two variables")
    print("Enter\'quit' to quit from programm")
    user_inp = input(":")

    if user_inp == "quit":
        break
    elif user_inp == "add":
        num1 = float(input("1)Variable = "))
        num2 = float(input("2)Variable = "))
        print(num1+num2)
    elif user_inp == "multiply":
        num1 = float(input("1)Variable = "))
        num2 = float(input("2)Variable = "))
        print(num1*num2)
    elif user_inp == "divide":
        num1 = float(input("1)Variable = "))
        num2 = float(input("2)Variable = "))
        print(num1/num2)
    elif user_inp == "Subtract":
        num1 = float(input("1)Variable = "))
        num2 = float(input("2)Variable = "))
        print(num1-num2)
    
