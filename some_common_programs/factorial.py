# The factorial of a number is the product of all the integers from 1 to that number

n = int(input("Enter a number : "))

fact = 1
for i in range(1, n+1):
    fact *= i
print("factorial of", n, "is", fact)
