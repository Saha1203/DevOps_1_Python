import sys

def add(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    sub = num1 - num2
    return sub

def mul(num1, num2):
    mul = num1 * num2
    return mul


num1 = float(sys.argv[1])
operation  = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    print(add(num1,num2))
elif operation == "sub":
    print(sub(num1, num2))
elif operation == "mul":
    print(mul(num1,num2))
else:
    print("Invalid Operation")

