# # Create a program that generates the Fibonacci sequence up to a given number of terms.
# def fibonoci(n):
#     if n==0 :
#         return 0
#     if n==1:
#         return 1
#     return fibonoci(n-1)+fibonoci(n-2)

# n=int(input("Enter the number of terms:"))
# print(fibonoci(3))


# # Implement a program that creates a multiplication table for a given number.
# def multiplication_table(n):
#     for i in range(1,11):
#         print(n,"*",i,"=",n*i)
# print(multiplication_table(2))    


# # Write a program that calculates the factorial of a given number.
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n *factorial(n-1)
# print(factorial(4))    


# # Create a loop that prints all prime numbers between 1 and 50.
# def prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#         return True    
# for number in range(1,50):
#     if prime(number):
#         print(number)


# # Write a program to count words which have characters greater than or equal to 5.
# def count_words(sentence):
#     words = sentence.split()
#     count = 0
#     for word in words:
#         if len(word) >= 5:
#             count += 1
#     return count
# print(count_words("The quick brown fox jumps over the lazy dog"))


# # Write a program to calculate the sum of digits in a number.
# def sum_digits(num):
#     sum = 0
#     while num:
#         sum += num % 10
#         num //= 10
#     return sum
# print(sum_digits(123))


# # Write a program that checks and sums the positive values in a given list.
# def sum_positive_values(lst):
#     sum = 0
#     for i in lst:
#         if i > 0:
#             sum += i
#     return sum
# print(sum_positive_values([1, 2, 3, -4, 5, -5]))


# # Write a program to check if the given string is a palindrome or not.
# def is_palindrome(s):
#     return s == s[::-1]
# print(is_palindrome("madam"))


# # Write a program to find the factorial of a given number using recursion.
# def factorial(n):
#     if n == 1 or n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(10))        


# # Write a program to return the square of all elements in a given list.
# def square_list(lst):
#     for i in range(len(lst)):
#         lst[i] = lst[i] * lst[i]
#     return lst
# print(square_list([2,3,4,5]))


# # Write a program that takes a given list and sorts it alphabetically.
# def sort_list(lst):
#     lst.sort()
#     return lst
# print(sort_list(["b", "c", "f", "a" , "g"]))


# # Write a program that takes two lists and returns the intersection (common elements) between them.
# def intersection(lst1,lst2):
#     lst3 = []
#     for i in lst1:
#         for j in lst2:
#             if i == j:
#                 lst3.append(i)
#     return lst3
# print(intersection([1,2,3,4,5],[1,2,3,7,8]))


# # Write a program that removes the vowels from a string and returns the modified string.
# def remove_vowel(s):
#     lst=list(s)
#     for i in lst:
#         if i in "aeiouAEIOU":
#             lst.remove(i)
#     return ''.join(lst)
        
# print(remove_vowel("hi i am sharjeel"))


# # Write a program to find the largest length of a word in a sentence.
# def largest_word(sen):
#     lst=sen.split()
#     max=0
#     for i in lst:
#         if len(i) > max:
#             max=len(i)
#     return max
# print(largest_word("i am sharjeel"))


# # Given a list of words, concatenate them into a single string with spaces.
# def concatinat_words(lst):
#     return ' '.join(lst)
# print(concatinat_words(["i", "am", "sharjeel"]))


# # Write a function to count the number of vowels in a string.
# def count_vowel(str):
#     lst=list(str)
#     count=0
#     for i in lst:
#         if i in "aeiouAEIOU":
#             count+=1
#     return count
# print(count_vowel("i am sharjeel"))


# # Given a list of names, count the number of names that start with a vowel.
# def list_of_names(lst):
#     count=0
#     for i in lst:
#         if i[0] == "A":
#             count+=1
#     return count
# print(list_of_names(["sharjeel","Ali","ahmed"]))


# # Write a function to remove all duplicate characters from a given string.
# def remove_duplicates(str):
#     lst=list(str)
#     for i in lst:
#         if lst.count(i) > 1:
#             lst.remove(i)
#     return ''.join(lst)
# print(remove_duplicates("sharjeel"))


# # Write a function that takes a sentence and a word as input and checks whether the word is present in the sentence or not.
# def word_existence():
#     sen=input("Enter any sentence ")
#     word=input("Enter any word ")
#     if word in sen:
#         print("Word is present in sentence")
#     else:
#         print("Word is not present in sentence")
# print(word_existence())        


# # Write a program that contains two lists and creates a new list that contains the common items from the two lists.
# def common_items(lst1,lst2):
#     lst3=[]
#     for i in lst1:
#         if i in lst2:
#             lst3.append(i)
#     return lst3
# print(common_items([1,2,3,4,5],[3,4,5,6,6]))
    

# # Write a program to count the occurrences of each word in a sentence.
# def count_occurrences(sen):
#     lst=list(sen.split())
#     for i in lst:
#         print(i,"=",lst.count(i))
# print(count_occurrences("sharjeel is a good boy"))


# Create a function that takes a list of strings and returns the list sorted by the frequency of occurrence.

# Create a function that takes a list of strings and returns the list sorted by length.

# # Create two dictionaries and merge them into one dictionary.
# dict1={"name":"Sharjeel"}
# dict2={"age":"21"}
# dict3=dict1 | dict2
# print(dict3)

# Write a program to find the most frequent item in a list.
