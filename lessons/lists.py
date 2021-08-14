#                                      --ACCESS TO LISTS--



# List items are ordered, mutable, and allow duplicate values.
#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets
#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))# result is 3

# Lists can contain any complex objects like functions, classes, modules and any data types like number, string..
a = [int, len, False, 'smth', 5]

#It is also possible to use the list() constructor when creating a new list:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#<class 'list'>


#                         --THE DIFFERENCE BETWEEN 'is' AND '==' OPERATORS IN LISTS--



fruits = ['apple', 'banana', 'peach', 'apricot', 'berry', 'orange', 'cherry', 'fig', 'lemon', 'lime']
print(fruits[:] == fruits)# The equality operator compares the values of both the operands and checks for value equality
print(fruits[:] is fruits)# The 'is' operator checks whether both the operands refer to the same object or not
# we can check whether objects are same or not  with id() fuction which returns the identity of an object . ID is an abbreviation of identity 
print(id(fruits))# the id of this object is 139682684097024
print(id(fruits[:]))# the id of this objects is 139682684097472. The id numbers of both objects are different
# So they are not same objects. So if we check them with 'is' operator it returns False
# Another example for same objects :
lists1 = []
lists2 = []
print(lists1 is lists2) # The result is False. Because they are not same objects. 
fruit = 'apricot'
print(fruit[1])
print(id(fruit)) # id number of this object is 139870060198960
print(id(fruit[:]))# id number of this object is 139870060198960
# As you can see they are the same objects. Because their id numbers are equal
print(fruit is fruit[:])# In string objects 'is' operator always return True for 'fruit' and 'fruit[:]'. In other situations it returns False if objects are not same 
# Proof of the sentence written above
name = 'Salohiddin'
print(name is fruit)# it returns False



#                             --WORKING WITH LIST INDEXES--



fruits = ['apple', 'banana', 'peach', 'apricot', 'berry', 'orange', 'cherry', 'fig', 'lemon', 'lime']
#            0,        1,       2,         3,       4,        5,        6,       7      8        9
#           -10       -9       -8         -7       -6        -5        -4       -3     -2       -1

print(fruits[0])# it returns 'apple'
print(fruits[1])# it returns 'banana'
print(fruits[-3])# it returns 'fig'
fruits1 = fruits[1:4]# it contains 'banana', 'peach', 'apricot'. Because fruits[1:4] means that 
# give me elements of the list from 1st element to 4th one(4th element('berry') is not included. fruits[1:4] returns 1,2,3th elements of the list)
#Quyida ko'rsatilgan misoldagi kabi(fruits[1:4]) listlar hech qachon reverse tartibda qiymatlarni chiqarmaydi.
#Agar u quyidagi kabi bo'lsa(fruits[-4:-1]) ham. fruits[-1:-4] -> ushbu obyekt bo'sh list qaytaradi. Chunki u reverse tartibdagi qiymatlarni olmoqchi.
#Faqat quyidagi holatdagina teskari qiymat olsa bo'ladi. Yani fruits[-1:-4:-1] ->ko'rib turganingizdek [-1:-4] reverse qiymat qaytaradi. agar u yolg'iz bo'lsa
#ishlamaydi, lekin reverseni ifodalaydigan yana bir qiymat qo'shsak u ishlaydi. Yani birinchi qism([(-1:-4):-1]) reverse bo'lsa
#ikkinchi qism[-1:-4:(-1)] ham reverse bo'lishi kerak.Misol: fruits[5:1:-1]result:orange, berry, apricot, peach.
#  Agar birinchi qism reverse bo'lmasa ikkinchi qism ham reverse bo'lmasligi kerak. Shunda ushbu 
#obyekt to'g'ri natija qaytaradi. Misol fruits[-5:-1:2] result: 5,7

print(fruits1)
fruits1 = fruits[:5]
print(fruits1)# it returns from 0th element of the list to 5th one(5th element is not included)

fruits1 = fruits[2:]
print(fruits1)# This returns from the second element to the last element(it includes also the last element)
fruits1 = fruits[-5:-2]
print(fruits1)# it returns from -5th element to -2th element(id does not include -2th element)
fruits1=fruits[:-5]
print(fruits1)# it returns from 0th element to the -5th element(it does not include -5th element)
fruits1 = fruits[-5:]
print(fruits1)# it returns from -5th element to the last element(it includes also the last element)
fruits1 = fruits[0:5:2]
print(fruits1)# it returns every second element from 0th one to 5th one(5th element is not included, 0th element is the second element, So it is included as a first every second element) 
# result : ['apple', 'peach', 'berry']
fruits1 = fruits[6:0:-2]
print(fruits1)# It returns every -2th element of the list from index 6 to index 0(index0 is not included)
fruits1 = fruits[-6::-2]
print(fruits1)# the result is ['berry', 'peach', 'apple']
print(fruits[-6:])# the result is ['berry', 'orange', 'cherry', ...]
print(fruits[::-1])# it returns the reverse of the list
fruits1 = fruits[-6:2:-1]
print(fruits1)# it returns ['berry', 'apricot']
fruits1 = fruits[::-2]
print(fruits1)
#



#                             --WORKING WITH CHANGE LIST ITEMS--



fruits = ['apple', 'banana', 'peach', 'apricot', 'berry', 'orange', 'cherry', 'fig', 'lemon', 'lime']
fruits[1] = 'pineapple'
print(fruits)# The 2th element('banana') has beeen changed to 'pineapple'
fruits[1:3] = ['kiwi', 'mango']
print(fruits)#   1st,     2nd     elements of the list has been changed to 
#              'kiwi', 'mango'
fruits[1] = 'mango', 'apple'
print(fruits)# it returns ('mango', 'apple')
fruits[5] = ['melon', 'strawbarrey']
print(fruits)# 5th element of the list has been changed to ['melon', 'strawberry']
fruits[1:3] = 'melon'
print(fruits)# 1st, 2nd, 3rd, 4th, 5th elements of the list has been changed to 
#              'm', 'e', 'l', 'o', 'n'
fruits[1:3] = ['melon']
print(fruits)# 1st, 2nd elements('m', 'e') of the list has been changed to 'melon',
print(fruits[1])# the result is 'melon'
fruits.insert(3, 'watermelon')
print(fruits)# it inserts 'watermelon' to the index 3



#                                       --ADD LIST ITEMS--



#To add an item to the end of the list, use the append() method:
thislist = ['apple', 'banana', 'cherry']
thislist.append('peach')
print(thislist)# result is ['apple', 'banana', 'cherry', 'peach']

#The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)# result is ['apple', 'orange', 'banana', 'cherry']

#To append elements from another list to the current list, use the extend() method:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)#result is ["apple", "banana", "cherry", "mango", "pineapple", "papaya"]

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)#result is ['apple', 'banana', 'cherry', 'kiwi', 'orange']

#we can add them also in this way
thislist = ["apple", "banana", "cherry"]
thistuple = ["kiwi", "orange"]
print(thislist + thistuple)#result is ['apple', 'banana', 'cherry', 'kiwi', 'orange']
smth = 'smth'
print(thislist + smth)# result is ['apple', 'banana', 'cherry', 's', 'm', 't', 'h']



#                                       --REMOVE LIST ITEMS--



#The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
smth = thislist.remove("banana")
print(thislist)#result is ['apple', 'cherry']
print(smth)# returns None

#The pop() method removes the specified index:
thislist = ["apple", "banana", "cherry"]
smth = thislist.pop(1)
print(thislist)#result is ['apple', 'cherry']
print(smth)#result is 'banana', pop() method saves the specified index while that method deletes it 

#If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)#result is ['apple', 'banana']

#The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)#result is ['banana', 'cherry']

#The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist#result is (this will cause an error because you have completely deleted "thislist")

#The clear() method empties the list.
#The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)#result is []



#                                       --LOOP LIST ITEMS--



#You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)# result is apple
                     #banana
                     #cherry

#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#You can loop through the list items by using a while loop:
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1 



#                                       --LIST COMPREHENSION--



#Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)#result is ['banana', 'cherry', 'kiwi', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)#result is ['apple', 'banana', 'cherry', 'kiwi', 'mango']


#The syntax of list comprehension:
# newlist = [expression for item in iterable if condition == True]

#Return the item if it is not banana, if it is banana return orange
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)#result is ['apple', 'orange', 'cherry', 'kiwi', 'mango']



#                                       --SORT LISTS--



#By default, sort() doesn't require any extra parameters. However, it has two optional parameters:
#'reverse' - If True, the sorted list is reversed (or sorted in Descending order)
#'key' - function that serves as a key for the sort comparison

#Note: The simplest difference between sort() and sorted() is: sort() changes the list directly and doesn't return any value, 
# while sorted() doesn't change the list and returns the sorted list.

#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)#result is ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)#result is [23, 50, 65, 82, 100]

#To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)#result is ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#Sort the numeric list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)#result is [100, 82, 65, 50, 23]

#You can also customize your own function by using the keyword argument key = function.
#The function will return a number that will be used to sort the list (the lowest number first):
#Sort the list based on how close the number is to 50:
def myfunc(n):
      return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)#result is [50, 65, 23, 82, 100]. 

#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)#result is ['Kiwi', 'Orange', 'banana', 'cherry']

#Luckily we can use built-in functions as key functions when sorting a list.
#So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi","Apricot", "cherry"]
thislist.sort(key = str.lower)
print(thislist)# result is ['Apricot', 'banana', 'cherry', 'Kiwi', 'Orange']

#What if you want to reverse the order of a list, regardless of the alphabet?
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)#result is ['cherry', 'Kiwi', 'Orange', 'banana']

#Sort the list according to each string's length. In this situation, list must contain only string data type
thislist = ["bananas", "Orange", "Kiwi", "cherries"]
thislist.sort(key=len)
print(thislist)#result is ['Kiwi', 'Orange', 'bananas', 'cherries']

#We know that a tuple is sorted using its first parameter by default.
#  Let's look at how to customize the sort() method to sort using the second element.
# take second element for sort
def takeSecond(elem):
    return elem[1]
# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
random.sort(key=takeSecond)
# print list
print('Sorted list:', random)#result: Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]

# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]
# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')

def get_age(employee):
    return employee.get('age')

def get_salary(employee):
    return employee.get('salary')

# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')

#results:
#[{'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}]

#[{'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}]

#[{'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}]

#Sort a list of integers based on
# their remainder on dividing from 7
  
def func(x):
    return x % 7
  
L = [15, 3, 11, 7]
  
print ("Normal sort :", sorted(L))
print ("Sorted with key:", sorted(L, key = func))
#Normal sort : [3, 7, 11, 15]
#Sorted with key: [7, 15, 3, 11]



#                                       --COPY LISTS--



#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
thislist = ["apple", "banana", "cherry"]
mylist = thislist
thislist[1]='apricot'
print(mylist)#result is ['apple', 'apricot', 'cherry']


#There are ways to make a copy, one way is to use the built-in List method copy():
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)#result is ['apple', 'banana', 'cherry']

#Another way to make a copy is to use the built-in method list():
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)#result is ['apple', 'banana', 'cherry']



#                                       --JOIN LISTS--



#There are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)#result is ['a', 'b', 'c', 1, 2, 3]

#Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)#result is ['a', 'b', 'c', 1, 2, 3]

#Or you can use the extend() method, which purpose is to add elements from one list to another list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)#result is ['a', 'b', 'c', 1, 2, 3]



#                                       --NESTED LISTS--



#You have seen that an element in a list can be any sort of object. That includes another list. 
# A list can contain sublists, which in turn can contain sublists themselves, and so on to arbitrary depth.
#     0                  1                     2         3        4    
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
#            0          1          2     3            0     1
print(x[1][0])
#'bb'
print(x[1][1])
#['ccc', 'ddd']
print(x[1][2])
#'ee'
print(x[1][3])
print(x[1][1][1])
#'ddd'
print(x[3][::-1])
#['ii', 'hh']



#                                       --DYNAMIC LISTS--



#When items are added to a list, it grows as needed:
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

a[2:2] = [1, 2, 3]
a += [3.14159]
print(a)
#result is ['foo', 'bar', 1, 2, 3, 'baz', 'qux', 'quux', 'corge', 3.14159]

#Similarly, a list shrinks to accommodate the removal of items:
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2:3] = []
del a[0]
print(a)
#['bar', 'qux', 'quux', 'corge']



#Searching index number of the list:



cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

result = cities.index('Osaka')
print(result)



cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
city = 'Osaka'

if city in cities:
    result = cities.index(city)
    print(f"The {city} has an index of {result}.")
else:
    print(f"{city} doesn't exist in the list.")
