#                                 --BOOLEANS--



#In programming you often need to know if an expression is True or False.
#You can evaluate any expression in Python, and get one of two answers, True or False.
#When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)#True
print(10 == 9)#False
print(10 < 9)#False

#The bool() function allows you to evaluate any value, and give you True or False in return:
print(bool("Hello"))#True
print(bool(15))#True

#Almost any value is evaluated to True  if it has some sort of content.

#Any string is True, except empty strings.

#Any number is True, except 0.

#Any list, tuple, set, and dictionary are True, except empty ones.

#In fact, there are not many values that evaluate to False,
#except empty values, such as (), [], {}, "", the number 0, and the value None.
#And of course the value False evaluates to False.
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#One more value, or object in this case, evaluates to False, and 
# that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
    def __len__(self):
      return 0
myobj = myclass()
print(bool(myobj))#False

#You can create functions that returns a Boolean Value:
def myFunction() :
      return True
print(myFunction())#True


#Python also has many built-in functions that return a boolean value, like the isinstance() function, 
# which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))#True

#Booleans are considered a numeric type in Python. This means they’re numbers for all intents and purposes. 
#In other words, you can apply arithmetic operations to Booleans, and you can also compare them to numbers:
#True = 1
#False = 0
print(True + False/True)#1
print(True + True)#2
print(True + 1)#2


