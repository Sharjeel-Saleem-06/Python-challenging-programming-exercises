# Write a program that read text filesa nd prints its contents.
with open("sharry.txt","r")as f:
    contents=f.read()
    print(contents)


# Create a new text file and write contents in it
with open ("file.txt","w")as new_file:
    new_file.write("Hi my name is sharjeel")


# Read a csv file and process its data
import csv
with open("titanic.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


# Write a python program to copyt the contents of one text file to another
with open("sharry.txt","r") as source:
    contents=source.read()
with open("test.txt","w") as destination:
    destination.write(contents)  


# GIVEN A CSV FILE WITH STUDENT NAMES AND SCORES FIND THE STUDENT WITH HIGHEST SCORE
import csv
with open("titanic.csv","r") as f:
    reader=csv.reader(f)
    data=list(reader)
    max_score=0
    max_student=""
    for row in data[1:]:
        score=int(row[1])
        if score>max_score:
            max_score=score
            max_student=row[0]
            print(max_student,max_score)


# Implement a  Function to count the number of words and lines in a text file
def count_words_and_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    return num_lines, num_words
filename = 'input.txt'
lines_count, words_count = count_words_and_lines(filename)