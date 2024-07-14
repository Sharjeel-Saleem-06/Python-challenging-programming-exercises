# Write  program to check that the entered number is even or odd
number=int(input("Enter any number"))
if number%2==0:
    print("Even number")
else:
    print("Odd number")

# Write a program to check weather the year is leap year or not
year=int(input("Enter any year ="))
if year%4==0:
    print("Leap year")
else:
    print("Not a leap year")

# Write a program to find euclidean distance between two points
x1=int(input("Enter value of x1="))
y1=int(input("Enter value of y1="))
x2=int(input("Enter value of x2="))
y2=int(input("Enter value of y2="))
D = ( x2 - x1 )**2 + ( y2 - y1 ) **2
print("Euclidean distance is",D)

# Write a program to ensure weather three angles can form triangle
a=int(input("Enter value of angle a="))
b=int(input("Enter value of angle b="))
c=int(input("Enter value of angle c="))
if a+b+c==180:
    print("Triangle can be formed")
else:
    print("Triangle can not be formed")

# Check weather the cost price is greater then selling price or not 
cost_price=int(input("Enter cost price="))
selling_price=int(input("Enter selling price="))
if cost_price>selling_price:
    print(f"Loss",cost_price - selling_price)
else:
    print(f"Profit",selling_price - cost_price)