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
#                                        --LOOP TUPLES--
#                                        --JOIN TUPLES--
#
#
