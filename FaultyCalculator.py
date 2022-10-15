"""The calculation of the following number will show the given wrong result.
45*3=555, 56+9=77, 56/6=4"""
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
op = input("Choose the operator: add, sub, mul, div: ")
if n1 == 45 and n2 == 3 and op == "mul":
    print(555)
elif n1 == 56 and n2 == 9 and op == "add":
    print(77)
elif n1 == 56 and n2 == 6 and op == "div":
    print(4)
else:
    if op == "add":
        print(n1+n2)
    elif op == "sub":
        print(n1-n2)
    elif op == "mul":
        print(n1*n2)
    elif op == "div":
        print(n1/n2)
    else:
        print("Invalid Input!")
