# for loop
# there is function in python named range which we use for generating sequence

# here range will generate 0 to 9 sequence
for i in range(10):
    print(i, end=", ")

print("\n------------------*****------------------")

# here range will generate 1 to 9 sequence
for i in range(1, 10):
    print(i, end=", ")

print("\n------------------*****------------------")

# here range will generate 1 to 10 sequence
for i in range(1, 11):
    print(i, end=", ")

print("\n------------------*****------------------")

# here range will generate 5 to 15 sequence
for i in range(5,16):
    print(i, end=", ")

print("\n------------------*****------------------")

# here range will generate 1 to 10 sequence with each step of 2
for i in range(1, 11, 2):
    print(i, end=", ")

print("\n------------------*****------------------")

# here range will generate 10 to 1 sequence
for i in range(10, 0, -1):
    print(i, end=", ")

print("\n------------------*****------------------")

# here range will generate 10 to 1 sequence with each step of 2
for i in range(10, 0, -2):
    print(i, end=", ")

print("\n------------------*****------------------")

# string in for
for i in "cmpundhir":
    print(i, end=", ")

print("\n------------------*****------------------")

# list in for
mylist = ["ram","shyam","sita","radha"]
print(type(mylist)) # type() is function to check type of an object
for i in mylist:
    print(i, end=", ")

print("\n------------------*****------------------")

# we can also add else after for loop like if statement
for i in range(5):
    print(i, end=", ")
    #if i==2:
    #    break
else:
    print("else working...")





