# Write a program to find  oldest age among 3 given ages

def oldestage():
    age1=(input('Enter your age'))
    age2=(input('Enter your age'))
    age3=(input('Enter your age'))
    if age1>age2 and age1>age3:
            print("age1 is greater ")
    elif age2>age1 and age2>age3:
            print("age2 is greater ")
    else:
        print("age3 is greater ")
    return True

print(oldestage())

# Write a program to convert celcius to fahrenheit
def celcius_to_fahrenheit():
    celcius=int(input("Enter temp in celcius"))
    fahrenheit=(celcius *9/5)+32
    print("temp in fahrenheit is",fahrenheit)

print(celcius_to_fahrenheit())


# Write a program to swap 2 number provided by user.
a=input("Enter a number to swap")
b=input("Enter a number to swap")
temp=a
a=b
b=temp
print("a=",a,"b=",b)


# Enter 3 number to sum
a=int(input("Enter number 1 to sum"))
b=int(input("Enter number 2 to sum"))
c=int(input("Enter number 3 to sum"))
sum=a+b+c
print(sum)


# Write a program to reverse 4 digit number and check if the reverse sequence is same as orignal input is same
a=input("Enter a 4 digit number")
if len(a)==4:
    print("number is 4 digit")
    print(a[::-1])
    if a[::-1]==a:
        print("palindrome")
    else:
        print("not palindrome")
else:
    print("number is not 4 digit")
    