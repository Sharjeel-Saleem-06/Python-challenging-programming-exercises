# Write a program to find simpe intrest
principle=int(input("Enter prinicpal value"))
rate=int(input("Enter rate of interest"))
time=int(input("Enter time in years"))
SI=(principle*rate*time)/100
print("Simple interest is",SI)

# write a program to find volume of clinder and calculate the cost when the cost of milk is 1 liter of milk is 40 Rs
from math import pi
height=int(input("Enter height of clinder"))
radius=int(input("Enter radius of clinder"))
volume=pi*height*radius**2
print(f"Volume:",volume)
cost_of_1_liter_milk=40
cost=volume*cost_of_1_liter_milk
print(f"cost:",cost)

# write a program to check
number=int(input("Enter any number"))
if number%3==0 and number%6==0:
    print("number is divisible by 3 and 6")
elif number%3==0:
    print("number is divisible by 3 only")
elif number%6==0:
    print("number is divisible by 6 only")
else:
    print("number is not divisible by 3 and 6")

# Write a program to find highest and lowset value in list
list=[1,2,3,4,5,6]
max=max(list)
min=min(list)
print(max,min)

# Write a program to check weather string is palidrome or not
string='poop'
if string[::-1]==string:
    print("palindrome")
else:
    print("not palindrome")
    

