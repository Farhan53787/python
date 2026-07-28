import random

inp = str(input("Want to roll dice? (yes/no) "))

if inp == "yes":
    print ( f"The number is : {random.randint(1,6)}")

elif inp == "no":
    print ("Have a nice day!")

else: 
    print("__Syntax  Error__")