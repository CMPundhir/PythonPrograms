# A function is a block of organized, reusable code that is used to perform a single, related action.
# which returns a value or does not return a value.


# function definition
def say_hello():
    print("ola...")


# function with a parameter
def say_hi(name):
    print("hi", name)


# default paramter function
def defaul_hi(name = "not found"):
    print("hi",name)


# named arguments example
def just_hello(fname, lname):
    print("welcome", fname, lname)


# variable arguments
def hello_to_all(*args):
    for a in args:
        print("hello",a)


# k arguments function where kwargs is a dictionary
def say_vip_hello(**kwargs):
    print(type(kwargs))
    a = kwargs["name"]
    print("vip hello",a)


# so to use a function you need to call it and this is known as 'function call'
say_hello()

say_hi("cmpundhir")

defaul_hi()
defaul_hi("ali")

just_hello("museed","ali")
just_hello(lname="pundhir", fname="cm")

hello_to_all("ali","cm","alan","yogesh","dalima")

say_vip_hello(name="cm",age=11)

