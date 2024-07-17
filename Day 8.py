# Write a program that will sum all positive number in list
listt = [1, 2, 3, 4, -1, -2, 1]
summ = 0  
for i in listt:
    if i > 0:
        summ += i  
print(summ)

# Create a program that takes a sentence an count the number of words in it
def sentence(sen):
    counts=sen.split()
    length=len(counts)
    return length
print(sentence("my name is sharry"))   

# Implement a program that swaps the vaues of two variables
a=input("Enter value=")
b=input("Enter value=")
temp=a
a=b
b=temp
print(f"Value of a =",a,"Valuse of b =",b)

# given a list of names concatinate them as a single string seperated by spaces
names = ["sharry", "sunny", "sunny", "sunny"]
print(" ".join(names))

# write a program to check if the string is panagram
pangram = "the quick brown fox jumps over the lazy dog"

alphabet = set('abcdefghijklmnopqrstuvwxyz')

string_set = set(pangram.lower())

if alphabet <= string_set:
    print("Pangram")
else:
    print("Not a pangram")

    
