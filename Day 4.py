# Task 1: Write a Python function that takes a list of numbers and returns the sum
# of all the numbers. Use a ‘for‘ loop and demonstrate the function with a sample
# list.
def sum_of_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
s=[1,2,3,4]
print(sum_of_numbers(s))    



# • Task 2: Create a Python script that reads a text file and counts the frequency of
# each word. Use a dictionary to store the word counts and display the top 10 most
# frequent words.
from collections import Counter
def word_counts(filepath):
    with open(filepath,'r')as file:
        text=file.read().lower()

    words= text.split()
    word_count=Counter(words)

    most_common_words=word_count.most_common(10)
    for word, count in most_common_words:
        print(f'{word}:{count}')

file_path=r"test.txt"
print(word_counts(filepath=file_path)   )     

    



# • Task 3: Implement a Python class called ‘Rectangle‘ that has attributes for width
# and height. Include methods to calculate the area and perimeter of the rectangle.
# Create an instance of the class and demonstrate the methods.


class Rectangle():
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        areaa=self.width*self.height
        return areaa

a=Rectangle(2,2)
print(a.area())

# • Task 4: Write a Python program that uses list comprehension to create a new list
# containing the squares of all even numbers from 1 to 20.

list=[1,2,3,4,5,6,7,8,9,10]
list1=[]
for i in range(1,21):
    if i%2==0:
        list1.append(i**2)

print(list1)



# Python Program to check Armstrong Number
# 1+5+3
def armgstrong(num):
    digits=str(num)       
    num_length=len(digits)

    total=sum(int(digit)**num_length for digit in digits)
    return total==num

print(armgstrong(153))