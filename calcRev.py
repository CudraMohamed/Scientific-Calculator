import math
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def sqrt(x):
    result=math.sqrt(x)
    return result

def exp(x):
    return x ** 2

def sin(x):
    result =math.sin(x)
    return result

def cos(x):
    result=math.cos(x)
    return result

def tan(x):
    result = math.tan(x)
    return result

print('''
Choose a number for the following operations:
1-Addition(x,y)
2-Subtraction(x,y)
3-Multiplication(x,y)
4-Division(x,y)
5-Square(x)
6-Square root(x)
7-sin(x)
8-cos(x)
9-tan(x)''')
op=int(input('What operation do you want to perform ? : '))

while op<10:
    if op ==1:
        print('enter the parametres')
        x1=int(input('enter x :'))
        y1=int(input('enter y : '))
        res1 =add(x1,y1)
        print("Addition = ", res1)
    elif op ==2:
        print('enter the parametres')
        x2=int(input('enter x :'))
        y2=int(input('enter y : '))
        res2 =subtract(x2,y2)
        print("Subtraction = ", res2)
    elif op ==3:
        print('enter the parametres')
        x3=int(input('enter x :'))
        y3=int(input('enter y : '))
        res3 =multiply(x3,y3)
        print("Multiplication = ", res3)
    elif op ==4:
        print('enter the parametres')
        x4=int(input('enter x :'))
        y4=int(input('enter y : '))
        res4 =divide(x4,y4)
        print("Division = ", res4) 
    elif op ==5:
        print('enter the parametres')
        x5=int(input('enter x :'))
        res5 =exp(x5)
        print("Square = ", res5)
    elif op ==6:
        print('enter the parametres')
        x6=int(input('enter x :'))
        res6 =sqrt(x6)
        print("Square root = ", res6)
    elif op ==7:
        print('enter the parametres')
        x7=int(input('enter x :'))
        res7 =sin(x7)
        print("sin = ", res7)
    elif op ==8:
        print('enter the parametres')
        x8=int(input('enter x :'))
        res8 =cos(x8)
        print("cos = ", res8)
    elif op ==9:
        print('enter the parametres')
        x9=int(input('enter x :'))
        res9 =tan(x9)
        print("tan = ", res9)
    else:
        print("Choose another operation")
    new=int(input("Do you want to continue ? -(Yes = 1,No = 0)"))
    if new ==1:
        op=int(input("Enter operation : "))
    elif new ==0:
        print("Thank you for using our scientific calculators")
        break
