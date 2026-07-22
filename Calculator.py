import math

choose = input("Do you want to calculate any number? (Type, Yes or No)")

if choose == "yes":

    while True: 

        Oper = input("Operation you want to perform (Type, |addition| |substraction| |multipication| |division| |exponentiation| |root| |sine| |cosine|) :")

        if Oper == "addition":
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(f"{num1} + {num2} = {num1 + num2}")

        elif Oper == "subtraction":
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(f"{num1} - {num2} = {num1 - num2}")

        elif Oper == "multiplication":
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(f"{num1} x {num2} = {num1 * num2}")

        elif Oper == "division":
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(f"{num1} ÷ {num2} = {num1 / num2}")

        elif Oper == "exponentiation":
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(f"{num1} ^ {num2} = {num1 ** num2}")

        elif Oper == "root":
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(f"{num1} ^ {1/num2} = {num1 ** (1/num2)}")

        elif Oper == "sine":
            num1 = int(input("Enter the number: "))
            print(f"sin({num1}) = {math.sin(math.radians(num1)):.2f}")

        elif Oper == "cosine":
            num1 = int(input("Enter the number: "))
            print(f"cos({num1}) = {math.cos(math.radians(num1)):.2f}")

        else: 
            print(" Error .... Out  of  the  list  of  the  operations ") 

        choose = input("Do you want to again calculate any number? (Type, Yes or No)")

        if choose == "yes":
                    Oper = input("Operation you want to perform (Type, |addition| |substraction| |multipication| |division| |exponentiation| |root| |sine| |cosine|) :")
            
                    if Oper == "addition":
                        num1 = int(input("Enter the first number: "))
                        num2 = int(input("Enter the second number: "))
                        print(f"{num1} + {num2} = {num1 + num2}")
            
                    elif Oper == "subtraction":
                        num1 = int(input("Enter the first number: "))
                        num2 = int(input("Enter the second number: "))
                        print(f"{num1} - {num2} = {num1 - num2}")
            
                    elif Oper == "multiplication":
                        num1 = int(input("Enter the first number: "))
                        num2 = int(input("Enter the second number: "))
                        print(f"{num1} x {num2} = {num1 * num2}")
            
                    elif Oper == "division":
                        num1 = int(input("Enter the first number: "))
                        num2 = int(input("Enter the second number: "))
                        print(f"{num1} ÷ {num2} = {num1 / num2}")
            
                    elif Oper == "exponentiation":
                        num1 = int(input("Enter the first number: "))
                        num2 = int(input("Enter the second number: "))
                        print(f"{num1} ^ {num2} = {num1 ** num2}")
            
                    elif Oper == "root":
                        num1 = int(input("Enter the first number: "))
                        num2 = int(input("Enter the second number: "))
                        print(f"{num1} ^ {1/num2} = {num1 ** (1/num2)}")
            
                    elif Oper == "sine":
                        num1 = int(input("Enter the number: "))
                        print(f"sin({num1}) = {math.sin(math.radians(num1)):.2f}")
            
                    elif Oper == "cosine":
                        num1 = int(input("Enter the number: "))
                        print(f"cos({num1}) = {math.cos(math.radians(num1)):.2f}")
            
                    else: 
                        print(" Error .... Out  of  the  list  of  the  operations ")
        else:
                    print("Have a good day!")
                    break
else:
    print("Have a good day!")