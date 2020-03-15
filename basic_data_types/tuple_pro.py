tuple1 = (10, 20, 30, 40, 50, 60)
print(tuple1)
count = 0
for i in tuple1:
    print("tuple1[%d] = %d" % (count, i))
    count += 1

print("--------------------------------------------------")

for i in range(len(tuple1)):
    print("tuple1[%d] = %d" % (i,tuple1[i]))

print("--------------------------------------------------")

# slice operator also works on tuple
print(tuple1[1:4])

print("--------------------------------------------------")

print(tuple1*2)

print("--------------------------------------------------")

print(tuple1 + tuple1)

print("--------------------------------------------------")

print(tuple("cmpundhir"))

print("--------------------------------------------------")

Employees = [(101, "Ayush", 22), (102, "john", 29), (103, "james", 45), (104, "Ben", 34)]
print("----Printing list----");
for i in Employees:
    print(i)
Employees[0] = (110, "David",22)
print();
print("----Printing list after modification----");
for i in Employees:
    print(i)