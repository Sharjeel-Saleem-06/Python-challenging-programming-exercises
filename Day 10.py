# Create  a program that generates fabinoci sequence upto given number of terms
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(3))


# Implement a program that create a mutiplication table of that number
def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

print(table(5))


# Write a program that calculates factorial of given number
def factorial(n):
    if n == 0 or n==1:
        return 1
    else: 
        return n * factorial(n-1)    
    
print(factorial(3))


# Create a loop that prints all prime number bw 1 t0 50:
def loops():
    for i in range(1,51):
        if i%2==0:
            continue
        else:
            print(i)

print(loops())

# Write a program to count words which have character greater then or equal to 5
def words():
    count=0
    words = ["hello", "world", "python", "is", "fun"]
    for word in words:
        if len(word) >= 5:
            count+=1
        else:
            continue
    print(f"{count}")        

words()

    

