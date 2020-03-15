Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(Days)
print(type(Days))
print("looping through the set elements ... ")
for i in Days:
    print(i)


print("--------------------------------------------------")

# using set() function to create a set
days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
Days = set(days_list)

Days.add("Holyday")
print(Days)

# discard() will delete element
Days.discard("Holiday")
print(Days)

# remove() will delete element and it will give KeyError on element not found
#Days.remove("Holiday")
#print(Days)

print("--------------------------------------------------")

Days1 = {"Monday","Tuesday","Wednesday","Thursday"}
Days2 = {"Friday","Saturday","Sunday","Monday","Wednesday"}
print(Days1 | Days2)  # printing the union of the sets using | operator
print(Days1.union(Days2))  # printing the union of the sets using union() function

print(Days1 & Days2)  # printing the intersection of the sets using & operator
print(Days1.intersection(Days2))  # printing the intersection of the sets using intersection() function

print(Days1-Days2)  # {"Tuesday", "Thursday" will be printed}
print(Days1.difference(Days2))

Days1.add("Monday")
Days1.update("Monday")




