# writea program to check if number is prime
def is_prime(num):
    if num %2==0:
        return False
print(is_prime(2))   

#create a function that cont number of vowels in string
def vowel_count(str):
    count=0
    for i in str:
        if i in 'aeiouAEIOU':
            count+=1
            return count
print(vowel_count("sharjeel"))
        
# Create a function that cound unique Words in a string
def count_unique_words():
    input_str = input("Enter a string: ")
    filter_string=input_str.replace(" ","")
    unique_words_set = set(filter_string)  
    print("Number of unique words:", len(unique_words_set))

count_unique_words()

# Create a function that cound unique letters in a string
def count_unique_letters():
    input_str = input("Enter a string: ")
    unique_words_set = set(input_str)  
    print("Number of unique words:", len(unique_words_set))

count_unique_letters()

# write a program to check the words starts with A
def check_words(str):
    words = str.split(" ")
    for word in words:
        if word[0] == "A" or word[0] == "a":
            print(word)

check_words("apple banana orange")
