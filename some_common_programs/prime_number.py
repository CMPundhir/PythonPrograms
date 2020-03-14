# those numbers which divides by themselves and 1 only are known as prime numbers

n = int(input("Enter a number : "))
if n == 1:
    isPrime = False
else:
    isPrime = True
for i in range(2, n):
    if n % i == 0:
        isPrime = False
        break
if isPrime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
