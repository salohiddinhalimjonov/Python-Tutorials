#                                            --LAMBDA FUNCTIONS--



#Python lambda expressions allow you to define anonymous functions.

#Anonymous functions are functions without names. The anonymous functions are useful when you need to use them once.

#A lambda expression typically contains one or more arguments, but it can have only one expression.

#lambda parameters: expression

#def anonymous(parameters):
#    return expression

#The following defines a function called get_full_name() that format the full name from the first name and last name:
def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)
#The get_full_name() function accepts three arguments:
#First name (first_name)
#Last name (last_name)   

def first_last(first_name, last_name):
    return f"{first_name} {last_name}"


def last_first(first_name, last_name):
    return f"{last_name}, {first_name}"

full_name = get_full_name('John', 'Doe', first_last)
print(full_name) # John Doe

full_name = get_full_name('John', 'Doe', last_first)
print(full_name) #  Doe, John   

#Instead of defining the first_last and last_first functions, you can use lambda expressions.

#For example, you can express the first_last function using the following lambda expression:
#lambda first_name,last_name: f"{first_name} {last_name}"
def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


full_name = get_full_name('John', 'Doe', lambda first_name,
                        last_name: f"{first_name} {last_name}")
print(full_name)

full_name = get_full_name('John', 'Doe', lambda first_name,
                        last_name: f"{last_name} {first_name}")
print(full_name)
#John Doe
#Doe, John

#Functions that return a function example:

def times(n):
    return lambda x: x * n

double = times(2)    
result = double(2)
print(result)#4

result = double(3)
print(result)#6

#Summary:
#Use Python lambda expressions to create anonymous functions, which are functions without names.
#A lambda expression accepts one or more arguments, contains an expression, and returns the result of that expression.
#Use lambda expressions to pass anonymous functions to a function and return a function from another function.