#                                        --FUNCTIONS--



#A function is a named code block that performs a job or returns a value.
#Sometimes, you need to perform a task multiple times in a program. And you don’t want to copy the code for that same task all over places.
#To do so, you wrap the code in a function and use this function to perform the task whenever you need it.
#For example, whenever you want to display a value on the screen, you just need to call the print() function. Behind the scene, Python runs the code inside the print() function to display a value on the screen.
#In practice, you use functions to divide a large program into smaller and more manageable parts. The functions will make your program easier to develop, read, test, and maintain.
def sum(a, b):
    return a + b


total = sum(10,20)
print(total)#30


#When you define a function, you can specify a default value for each parameter.
#def function_name(param1, param2=value2, param3=value3, ...):
def greet(name, message='Hi'):
    return f"{message} {name}"


greeting = greet('John')
print(greeting)#Hi John




def greet(name='there', message='Hi'):
    return f"{message} {name}"


greeting = greet('Hello')
print(greeting)#Hi Hello



def greet(name='there', message='Hi'):
    return f"{message} {name}"


greeting = greet(message='Hello')
print(greeting)#Hello there


#                                          --RECURSIVE FUNCTIONS--



#A recursive function is a function that calls itself until it doesn’t.
#Also, a recursive function needs to have a condition to stop calling itself.
# So you need to add an if statement like this:
#def fn():
    # ...
#    if condition:
        # stop calling itself
#    else:
#        fn()
    # ...

#Typically, you use a recursive function to divide a big problem 
# that’s difficult to solve into smaller problems that are easier-to-solve
def count_down(start):
    """ Count down from a number  """
    print(start)

    # call the count_down if the next
    # number is greater than 0
    next = start - 1
    if next > 0:
        count_down(next)


count_down(3)
#result:
#1
#2
#3



def sum(n):
    if n > 0:
        return n + sum(n-1)
    return 0


result = sum(5)
print(result)#15


def sum(n):
    return n + sum(n-1) if n > 0 else 0


result = sum(100)
print(result)#5050



#                                   --*args, **kwargs--



def add(*args):
    print(type(args))
    print(args)

add()
#result:
#<class 'tuple'>
#()


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


total = add(1, 2, 3)
print(total)#6




def add(x, y, *args, z):
    return x + y + sum(args) + z

add(10, 20, 30, 40, 50)#Type Error

#To fix it you need to use a keyword argument after the *args argument as follows:
def add(x, y, *args, z):
    return x + y + sum(args) + z

add(10, 20, 30, 40, z=50)



#                                      --Unpacking Arguments--



def point(x, y):
    return f'({x},{y})'
a = (0, 0)
origin = point(a)#Type Error : point() missing 1 required positional argument: 'y'

#To fix it you need to prefix the tuple a with the operator * like this:

def point(x, y):
    return f'({x},{y})'


a = (0, 0)
origin = point(*a)
print(origin)
#result: (0,0)


#**KWARGS

#When a function has the **kwargs parameter, it can accept a variable number of keyword arguments as a dictionary.
def connect(**kwargs):
    print(type(kwargs))
    print(kwargs)

connect()    
#result:
# <class 'dict'>
#{}    


def connect(**kwargs):
    print(kwargs)


config = {'server': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'Py1thon!Xt12'}

connect(**config)
#result:
#<class 'dict'>
#{'server': 'localhost', 'port': 3306, 'user': 'root', 'password': 'Py1hon!Xt'}

#The fn function can accept a variable number of the positional arguments. 
# Python will pack them as a tuple and assign the tuple to the args argument.
#The fn function also accepts a variable number of keyword arguments. 
#Python will pack them as a dictionary and assign the dictionary to the kwargs argument.
def fn(*args, **kwargs):
    print(args)
    print(kwargs)
fn(1, 2, x=10, y=20)    
#results:
#(1, 2)
#{'x': 10, 'y': 20}     

