# Implement a function that remvoes a key value pair from dict.
def remove_key_value_pair(dictionary, key):
    dictionary.pop(key,None)
    return dictionary
my_dict={"name":"Sharjeel",
         "age":25,
         "sem":"6"
         }
dict_to_remove= "name"
print(remove_key_value_pair(my_dict,dict_to_remove))  


# Create a program to check if two sets have any elemnt in common.
def check_common_elment(set1,set2):
    return set1.intersection(set2)
set1={1,2,3,4,5}
set2={3,4,5,6,7}
print(check_common_elment(set1,set2))


# Given two sets, find the union, intersection, and difference between them
def set_operations(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2  
    return union, intersection, difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union, intersection, difference = set_operations(set1, set2)
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)


# Create a function that takes a list of dictionaries and sorts them based on a specified key
def sort_dicts_by_key(dict_list, key):
    return sorted(dict_list, key=lambda x: x[key])
dict_list = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 28}
]
sorted_dicts = sort_dicts_by_key(dict_list, 'age')
print(sorted_dicts)


# Write a program that finds the average value of all the elements in a list of dictionaries
def average_value(dict_list, key):
    total = sum(d[key] for d in dict_list if key in d)
    count = sum(1 for d in dict_list if key in d)
    return total / count if count > 0 else 0
dict_list = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 28}
]
avg_age = average_value(dict_list, 'age')
print("Average age:", avg_age)


# need revision