#                                      --OPERATORS--



#Python divides the operators in the following groups:



#                                     --Arithmetic operators--



# Arithemic operators:  +, -, *, /, %, **, //
x = 8
y = 3
print(x + y)#11
print(x - y)#5
print(x * y)#24
print(x / y)#8/3
print(x % y)#residue(qoldiq): 2
print(x ** y)# quadrate(kvadrat): 512
print(x // y)#the floor division // rounds the result down to the nearest whole number: 2



#                                     --Assignment operators--



#Assignment operators: +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
x = 5
x+=3 # Addition : 8
x -= 3 # Subtraction : 5
x *= 3 # Multiplication : 15 
x /= 3 # Division : 5
x %= 3 # Modulus(qoldiq) : 2
x //= 3 # Floor Division(bo'ladi va natijani yaxlitlaydi) : 0
x = 3
x **= 3 # Exponentation : 27
x &= 3 # 
x |= 3 #
x ^= 3 #
x >>= 3 #
x <<= 3 #
print(x)

#                                     --Comparison operators--



#Comparison operators: ==, !=, >, <, >=, <=
x = 5
y = 4
print(x == y) # False
print(x != y) # True
print(x > y) # True
print(x < y) # False
print(x >= y) # True
print(x <= y) # False



#                                     --Logical operators--



# Logical operators: 
#and :  returns True if both statements are True: x<5 and x<10  (result : False)
#or : returns True if one of the statements is True: x>3 or x<4 (result : True)
#not : reverse the result, returns False if the result is True: not(x<5 and x<10) (result: True)



#                                     --Identity operators--



# Identity operators : is(returns True if both variables are the same object : x is y(result is False)), 
# is not(returns True if both variables are not the same object: x is not y(result is False))



#                                     --Membership operators--



x = 'banana'
y = ['apple', 'banana']
# in(returns True if a sequence with the specified value is present in the object : x in y (result is True))
# not in(returns True if a sequence with the specified value is not present in the object : x not in y (result is False))



#                                     --Bitwise operators--



# Not understandable.


#NONE:
#None is not the same as False.
#None is not 0.
#None is not an empty string.
#Comparing None to anything will always return False except None itself.
# Declaring a None variable
var = None

if var is None: # Checking if the variable is None
  print("None")#this is the result
else:
  print("Not None")