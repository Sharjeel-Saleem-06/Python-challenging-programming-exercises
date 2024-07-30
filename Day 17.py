# # Implement a program that reads a text file and counts the number of words and lines in it.
# def read_files():
#     with open ("test.txt","r") as f:
#         lines=f.readlines()
#         word_count=sum(len(line.split())for line in lines)
#         return len(lines),word_count
# print(read_files())    

 
# Create a function that takes a list of sentences and writes them to a new text file, each on a new line.
def take_sentence(sentences):
    with open("sharry.txt","w") as r:
        for sentence in sentences:
            r.write(sentence)
sentences=["hi i am sharjeel","Python is fun"]      
print(take_sentence(sentences))      
# Given a CSV file with employee details (name, age, salary), calculate the average salary of all employees.
# Write a program that reads a CSV file and finds the total sales revenue for a specific product.
# Given a text file with a list of numbers, write a function that finds the sum of all numbers in the file