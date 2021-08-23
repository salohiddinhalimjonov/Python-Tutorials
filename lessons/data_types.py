#                               --DATA TYPES--
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset(x = frozenset({"apple", "banana", "cherry"}))
#Boolean Type:	bool
#Binary Types:	bytes, bytearray(x = bytearray(5)), memoryview(x = memoryview(bytes(5)))

#You can get the data type of any object by using the type() function:

x = 5
print(type(x)) #<class 'int'>


#Python’s integer, float, boolean, string and tuple are immutable, means once assigned value to a variable it’s value can not be changed.
number1 = 10
print(id(number1)) # 54032216
number2 = number1
print(id(number2)) # 54032216

number1 = 20

print(number1) # 20
print(number2) # 10 how?

print(id(number1)) # 54032333 <-- noticed?
print(id(number2)) # # 54032216


address = (17, "street", 1222.22, 333.77)
address[1] = "india"

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment


#But here is a catch! what if the tuple contains mutable type values such as list, let’s check
address = (17, "street", [1222.22, 333.77])
address[2].append(1000)
print(address) # (17, 'street', [1222.22, 333.77, 1000])


#We can use the slice operator to copy an list and assign it to another.

items = [1, 2, 3]
numbers = items[:]

print(items) # [1, 2, 3]
print(numbers) # [1, 2, 3]

print(id(items)) # 59579608
print(id(numbers)) # 5957928

numbers[2] = "python"

print(items) # [1, 2, 3]
print(numbers) # [1, 2, "python"]

#By printing the memory location of two lists we can see that 
#the lists are pointing to two different memory locations and change in one list has not affected the another list.

from copy import copy
items = [1, 2, 3]
numbers = copy(items)

print(items) # [1, 2, 3]
print(numbers) # [1, 2, 3]

print(id(items))  # 52419600
print(id(numbers)) # 52465296

numbers[2] = "python"

print(items) # [1, 2, 3]
print(numbers) # [1, 2, "python"]
#we achieved the same functionality by using copy (Shallow copy).
#The Shallow copy is mostly used to copy when the argument has a compound data structure such as list, dict etc.


