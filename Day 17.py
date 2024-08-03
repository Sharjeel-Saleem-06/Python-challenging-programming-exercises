# Implement a program that reads a text file and counts the number of words and lines in it.
def read_files():
    with open ("test.txt","r") as f:
        lines=f.readlines()
        word_count=sum(len(line.split())for line in lines)
        return len(lines),word_count
print(read_files())    

 
# Create a function that takes a list of sentences and writes them to a new text file, each on a new line.
def take_sentence(sentences):
    with open("sharry.txt","w") as r:
        for sentence in sentences:
            r.write(sentence)
sentences=["hi i am sharjeel","Python is fun"]      
print(take_sentence(sentences))      


# Given a CSV file with employee details (name, age, salary), calculate the average salary of all employees.
import csv
def calculate_average_salary(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        salaries = [float(row['salary']) for row in reader]
    return sum(salaries) / len(salaries)

avg_salary = calculate_average_salary('employees.csv')
print(f"Average Salary: {avg_salary}")


# Write a program that reads a CSV file and finds the total sales revenue for a specific product.
import csv
def total_sales_revenue(file_path, product_name):
    total_revenue = 0
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['product'] == product_name:
                total_revenue += float(row['revenue'])
    return total_revenue

revenue = total_sales_revenue('sales.csv', 'Product A')
print(f"Total Revenue for Product A: {revenue}")

# Given a text file with a list of numbers, write a function that finds the sum of all numbers in the file.
def sum_numbers_in_file(file_path):
    with open(file_path, 'r') as file:
        return sum(int(line.strip()) for line in file)

total_sum = sum_numbers_in_file('numbers.txt')
print(f"Total Sum: {total_sum}")