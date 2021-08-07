#                                        --ACCESS TO TUPLES--


mytuple = ("apple", "banana", "cherry")
#Tuples are used to store multiple items in a single variable.
#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List,
#  Set, and Dictionary, all with different qualities and usage.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))#<class 'tuple'>
#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)#('apple', 'banana', 'cherry')
#You can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])#banana
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
#('foo', 'bar', 'baz', 'qux', 'quux', 'corge')

print(t[0])
#'foo'
print(t[-1])
#'corge'
print(t[1::2])
#('bar', 'qux', 'corge')
print(t[::-1])
#('corge', 'quux', 'qux', 'baz', 'bar', 'foo')




#                                        --UPDATE TUPLES--



#Once a tuple is created, you cannot change its values.
#Tuples are unchangeable, or immutable as it also is called.

#But there is a workaround. You can convert the tuple into a list, change the list,
#and convert the list back into a tuple. 
# . 

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), 
# create a new tuple with the item(s), and add it to the existing tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)#('apple', 'banana', 'cherry', 'orange')



#                                        --UNPACK TUPLES--



#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)#apple
print(yellow)#banana
print(red)#cherry
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)#apple
print(yellow)#banana
print(red)#['cherry', 'strawberry', 'raspberry']
#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)#apple
print(tropic)#["mango", "papaya", "pineapple"]
print(red)#cherry



#                                        --LOOP TUPLES--



#You can loop through the tuple items by using a for loop.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)#apple
          #banana
          #cherry

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])#apple
                     #banana
                     # cherry         
#You can loop through the list items by using a while loop.
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#apple
#banana
#cherry



#                                        --JOIN TUPLES--



#To join two or more tuples you can use the + operator:
#Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)#('a', 'b', 'c', 1, 2, 3)

#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)#('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
