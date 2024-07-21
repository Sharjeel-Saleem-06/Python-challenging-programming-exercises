# Write a program that takes 2 list and return intersection(common) between two lists
def intersection(lst1,lst2):
    lst0=[]
    for i in lst1:
        for r in lst2:
            if [i]==[r]:
                lst0.append(i)           
    return lst0
lst1=[1,2,3,4]
lst2=[2,3,5,6]
print(intersection(lst1,lst2))


# Write a program that remove the vowels and return modified string
def remove_vowels(str):
    vowels = "aeiouAEIOU"
    for i in vowels:
        str=str.replace(i,"")
    return str

str="My name is Sharjeel"
print(remove_vowels(str))


# Write a program to find the largest length of word in a sentence
def longest_length_of_word(sen):
    sen=sen.split()
    max_len=0
    for i in sen:
        if len(i)>max_len:
            max_len=len(i)
    return max_len

sen="MY name is Muhammad Sharjeel "
print(longest_length_of_word(sen))


# Given a list of words concatinate them into single string with spaces
def list_of_words(lst):
    str1=(" ".join(lst))
    return str1

lst=["hello","world","python","is","fun"]
print(list_of_words(lst))


#Write a function to count number of vowels in a string
def vowels_count(str):
    count=0
    for i in str:
        if i in 'AEIOUaeiou':
            count+=1
    return count
str='Sharjeel'
print(vowels_count(str))        



