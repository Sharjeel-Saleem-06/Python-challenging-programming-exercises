# Question 1:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

n=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        n.append(i)
        
print(n)            


# # Question 2:
# # Write a program which can compute the factorial of a given numbers.
# # The results should be printed in a comma-separated sequence on a single line.
# # Suppose the following input is supplied to the program:
# # 8
# # Then, the output should be:
# # 40320
#  fact of 0 and 1 is always 1

def factorial(n):
    if n==0 or n==1:          
        return 1    
    else:
        return n*factorial(n-1)

print(factorial(3))




#  Question:
#  With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
#  Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def dict(n):
     dict={}
     for i in range (1,n+1):
         dict[i]=i*i
     return dict
print(dict(4))    

#  Question:
#  Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
#  Suppose the following input is supplied to the program:
#  34,67,55,33,12,98
#  Then, the output should be:
#  ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


# # Question:
# # Define a class which has at least two methods:
# # getString: to get a string from console input
# # printString: to print the string in upper case.
# # Also please include simple test function to test the class methods.

class StringManipulator:
    
    def getString(self):
        self.string = input("Enter a string: ")
    
    def printString(self):
        print(self.string.upper())

def test_string():
    sm = StringManipulator()
    sm.getString()       
    sm.printString()      

test_string()

# # ------------------------------------------------------------#