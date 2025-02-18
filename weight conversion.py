weight = float(input("Please enter your weight: "))
unit = input("(K)g or (L)bs: ")

conversion =  unit.upper()
if conversion == "L":
    print("Your weight is " + str(weight * 0.45) + "Kg")
else:
    print("your weight is " + str(weight * 2.2) + "lbs")