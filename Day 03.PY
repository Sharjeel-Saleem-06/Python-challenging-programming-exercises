# Python program to add two numbers
num1=10
num2=20
add=num1+num2
print("The sum of two numbers is",add)

# Maximum of two numbers in Python
a=10
b=20
if a<b:
    print("b is greater than a")
else:
    print("a is greater than b")

# Python Program for factorial of a number
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fact(n-1)
print(fact(4) )  


# Python Program for simple interest
def simple_intrest():
    p = int(input("Enter the principal amount: "))
    r = int(input("Enter the rate of interest: "))
    t = int(input("Enter the time period: "))
    simpe_intrest=(p*r*t)/100
    print("The simple interest is",simpe_intrest)

simple_intrest()

