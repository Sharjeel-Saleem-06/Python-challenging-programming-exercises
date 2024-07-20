# Write a program to calculate sum of digits in a number
def calculate(num):
    sum=0
    number=str(num)
    for i in number:
        sum=sum+int(i)
    return sum    

print(calculate(123))

# Write a program that check and sum the positive values in a given list
def positive_number():
    sum=0
    num=[2,3,4,5,-1,2,-3]
    for i in num:
        if i>0:
            sum=sum+i
    return sum
print(positive_number())        

# Write a program to check if the given string is palindrome or not
def is_palindrome(str):
    if str==str[::-1]:
        return True
    else:
        return False
print(is_palindrome("bobe"))

# Write a program to find factorial of given number by recursion
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(3))    

# Write a program to return a square of all elements in a givn list
def square():
    lst=[1,2,3,4]
    for i in lst:
     print( i**2)
    
print(square())

# # Write a program that takes  given list and sort them alphabtically
def sort_alphabetically(given_list):

    sorted_list = sorted(given_list)
    return sorted_list

input_list = ["banana", "apple", "cherry", "date"]
sorted_list = sort_alphabetically(input_list)
print("Original list:", input_list)
print("Sorted list:", sorted_list)