# 1. Write a program to find the oldest age among 3 given ages.
age1=input("Enter your age = ")
age2=input("Enter your age = ")
age3=input("Enter your age = ")
if age1>age2 and age1>age3:
    print("The oldest age is",age1)
elif age2>age1 and age2>age3:
    print("The oldest age is",age2)
else:
    print("The oldest age is",age3)

# 2. Write a program to convert Celsius to Fahrenheit.
celsius = float(input("Enter temperature in celsius = "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in fahrenheit = ",fahrenheit)


# 3. Write a program to swap 2 numbers provided by the user.
num1=input("Enter num 1")
num2=input("Enter num 2")
temp=num1
num1=num2
num2=temp
print("num1 = ",num1)
print("num2 = ",num2)


# 4. Write a program to sum 3 given numbers.
num1=input("Enter num 1")
num2=input("Enter num 2")
num3=input("Enter num 3")
sum=int(num1)+int(num2)+int(num3)
print("Sum = ",sum)


# 5. Write a program to reverse a 4-digit number and check if the reverse sequence is the same as the original input (palindrome check).
def palindrome():
    number=input("Enter any number")
    if len(number)==4:
        reverse=number[::-1]
        if reverse==number:
            print("The number is palindrome")
            return True    
        else: 
            print("Number is not paindrome")  
            return False  
    else:
        print(" Kindly enter 4 digit number")
        quit()
print(palindrome())


# 6. Write a program to check if the entered number is even or odd.
num=int(input("Enter any number"))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")


# 7. Write a program to check whether the year is a leap year or not
year=int(input("Enter year"))
if (year % 4 == 0 and year % 100 != 0) or(year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")   


# 8. Write a program to find the Euclidean distance between two points.
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
x1=int(input("Enter x1"))
y1=int(input("Enter y1"))
x2=int(input("Enter x2"))
y2=int(input("Enter y2"))
print(distance(x1,y1,x2,y2))

# 9. Write a program to ensure whether three angles can form a triangle.
def triangle(a,b,c):
    if a+b+c==180 and a > 0 and b > 0 and c > 0:
        print("Triangle can be formed")
    else:
        print("Triangle cannot be formed")
a=int(input("Enter angle 1"))
b=int(input("Enter angle 2"))
c=int(input("Enter angle 3"))
triangle(a,b,c)


# 10. Check whether the cost price is greater than the selling price or not (calculate profit/loss).
cost=int(input("Enter cost price"))
selling=int(input("Enter selling price"))
if cost>selling:
    print("Loss",cost-selling)
else:
    print("Profit",selling-cost)


# 11. Write a program to find the simple interest.
p=int(input("Enter principal amount"))
r=int(input("Enter rate of interest"))
t=int(input("Enter time period"))
si=(p*r*t)/100
print("Simple interest is",si)


# 12. Write a program to find the volume of a cylinder and calculate the cost when the cost of milk of 1 liter of milk is 40 Rs.
r=int(input("Enter radius"))
h=int(input("Enter height"))
v=3.14*r*r*h
print("Volume of cylinder is",v)
milk=40
cost_of_milk=1*40
print(cost_of_milk)


# 13. Write a program to check if the entered number is divisible by 3 and/or 6
num=input("Enter number")
if num%3==0 and num%6==0:
    print("Divisible by 3 and 6")
else:
    print("Not divisible by 3 and 6")


# 14. Write a program to find the highest and lowest value in a list.
list=[1,2,3,4,5,6,7,8,9]
print("Highest value is",max(list))
print("Lowest value is",min(list))


# 15. Write a program to check whether a string is a palindrome or not.
str=input("Enter string")
rev=str[::-1]
if str==rev:
    print("Palindrome")
else:
    print("Not palindrome")


# 16. Write a program that will sum all positive numbers in a list.
list=[1,2,-3,4,-5,6,-7,8,-9]
sum=0
for i in list:
    if i>0:
        sum +=i
print(sum)


# 17. Create a program that takes a sentence and counts the number of words in it.
sentence=input("Enter sentence")
words = sentence.split(" ")
print("Number of words in sentence is",len(words))

# 18. Implement a program that swaps the values of two variables.
val1=input("Enter value 1 to swap")
val2=input("Enter value 2 to swap")
temp=val1
val1=val2
val2=temp
print(val1,val2)


# 19. Given a list of names, concatenate them as a single string separated by spaces.
names=["Rahul","Shivam","Rahul","Shivam","Roy"]
name=(" ").join(names)
print(name)


# 20. Write a program to check if a string is a pangram.
str=input("Enter string")
str=str.lower()
str=str.replace(" ","")
if len(str)==26:
    print("Pangram")
else:
    print("Not pangram")


# 21. Write a program to check if a number is prime.
num=int(input("Enter number"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print("Not prime")
            break
        else:
            print("Prime")
            break


# 22. Create a function that counts the number of vowels in a string.
def vowel_count(str):
    count = 0
    str1=str.lower()
    vowel_count=["a","e","i","o","u"]
    for i in str1:
        if i in vowel_count:
            count+=1
    return count
print(vowel_count("The quick brown fox jumps over the lazy dog"))


# 23. Create a function that counts unique words in a string.
def unique_words(str):
    str1=str.split()
    str2=set(str1)  #set is use to find unique words
    return len(str2)
print(unique_words("The quick brown fox jumps over the lazy dog"))


# 24. Create a function that counts unique letters in a string.
def unique_letters(str):
    str1=str.lower()
    str2=str1.replace(" ","")
    str3=set(str2)
    return len(str3)
print(unique_letters("The quick brown fox jumps over the lazy dog"))


# 25. Write a program to check words that start with the letter 'A'.
str=input("Enter string")
str1=str.split()
for i in str1:
    if i[0]=="A" or i[0]=="a":
        print( "Yes it starts with A")
    else:
        print("No it does not start with A")
