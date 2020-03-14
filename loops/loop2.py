# while loop
# we use while loop only when there is uncertain number of iteration

# while takes a expression whose output should be boolean
# infinite loop

while not True:
    print("hahahahhahhahahaha.....")

print("\n------------------------------------")

# if expression output is 0 it will be considered as false else run for infinite
while 0:
    print("huh... 10")

print("\n------------------------------------")

# this is just a for loop in while
i = 0
while i < 10:
    print(i, end=", ")
    i += 1

# this loop will terminate only when user enters 0
while (int(input("enter wa number"))) != 0:
    print("hiihihihihi....")
else:
    print("you entered 0 , exit")
