# Question 01:
# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

import datetime
now = datetime.datetime.now()
print(now)


#Question 03  Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

r=int(input("Enter value of radius"))
pi=3.14
area=r*pi
print("Area of circle is",area)


# # Question04: Write a  Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
firstname=input("Enter firstname")
lastname=input("Enter lastname")
print(lastname,"",firstname)

# #Question 05: Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# # Sample data : 3, 5, 7, 23
# # Output :
# # List : ['3', ' 5', ' 7', ' 23']
# # Tuple : ('3', ' 5', ' 7', ' 23')

n=input("Enter comma seperated nymber")
list=n.split(",")
tuple=tuple(list)
print("List:",list)
print("tUpl",tuple)

# Question 06: Write a  Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java
n=input("Enter filename")
print(n.split(".")[1]) 
print(n)
print(n.split(".")[0]) 


# Question 07: Write a  Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1])


# Question 08: Write a  Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i" % exam_st_date)

# Questin09: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

n=5
print(n + int(f"{n}{n}") + int(f"{n}{n}{n}"))


# Question 10: Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
from datetime import date
sample_date1=date(2014, 7, 2)
sample_date2=date(2014, 7, 11)
print(sample_date2-sample_date1)