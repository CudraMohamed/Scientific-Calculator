import math     #for inbuilt function to calculate scientific operations
#operations in the calculator
def add(a,b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def sqrt(a):               #for you to find the squareroot of a number, the number must be greater than 0
    result = math.sqrt(a)  #returns the square root of a number
    return result

def exp(a):  #exponentiation //the value for the exponent is 2
    return a ** 2   #to get the suare of a number

def sin(x):   #sine of a parameter using the math module
    result = math.sin(x)
    return result

def cos(x):
    result = math.cos(x)  #cosine of the parameter
    return result

def tan(x):
    result = math.tan(x)  #tan of the parameter
    return result

#Choosing the operation //use of a comment because of lack of gui for user interface
print("""
Choose a number for the following operations :
1 - Addition(x,y)
2 - Subtraction(x,y)
3 - Multiplication(x,y)
4 - Divide(x,y)
5 - Square(x)
6 - Square root(x)
7 - sin(x)
8 - cos(x)
9 - tan(x)""")
opr = int(input('What operation do you want to perform ?'))

#calculator script condition to get input from the user
while opr < 10:
    if opr == 1:
        print("enter the parameters")
        x1 = int(input("Enter x : "))
        y1 = int(input("Enter y : "))
        res1 = add(x1, y1)
        print("Addition = ",res1)
    elif opr == 2:
        x2 = int(input("Enter x : "))
        y2 = int(input("Enter y : "))
        res2 = add(x2, y2)
        print("Subtraction = ",res2)
    elif opr == 3:
        x3 = int(input("Enter x : "))
        y3 = int(input("Enter y : "))
        res3 = add(x3, y3)
        print("Multiplication = ",res3)
    elif opr == 4:
        x4 = int(input("Enter x : "))
        y4 = int(input("Enter y : "))
        res4 = add(x4, y4)
        print("division = ",res4)
    elif opr == 5:
        x5 = int(input("Enter x : "))
        res5 = exp(x5)
        print("Square = ",res5) 
    elif opr == 6:
        x6 = int(input("Enter x : "))
        res6 = sqrt(x6)
        print("Square root = ",res6) 
    elif opr == 7:
        x7 = int(input("Enter x : "))
        res7 = sin(x7)
        print("sin(x) = ",res7)
    elif opr == 8:
        x8 = int(input("Enter x : "))
        res8 = cos(x8)
        print("cos(x) = ",res8)
    elif opr == 9:
        x9 = int(input("Enter x : "))
        res9 = tan(x9)
        print("tan(x) = ",res9) 

    else:
        print('choose another operation')
    new = int(input("do you want to continue - (yes -1), (NO -0) : ")) 
    if new == 1:
        opr = int(input("Enter operation : "))
    elif new == 0:
        print("Thank for using the scientific calculator")
        break