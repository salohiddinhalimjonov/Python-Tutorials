#                                --SET--



#Sets are used to store multiple items in a single variable.
#Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
#A set is a collection which is both unordered and unindexed.
#Sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)#{'apple', 'cherry', 'banana'}
# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.

#Sets are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can add new items.
#Sets cannot have two items with the same value.

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)#{'banana', 'cherry', 'apple'}



#                                         --ACCESS TO LIST ITEMS--



#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
#by using the in keyword.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)#apple
          #banana
          #cherry


thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) #True 

#To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)#{'cherry', 'banana', 'apple', 'orange'}

#To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)#{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)#{'cherry', 'apple'}

#Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")#Note: If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)#{'apple', 'cherry'}

#You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
#The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item,  result:banana
print(thisset) #the set after removal,  result: {'apple', 'cherry'}
#Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)#set()

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) #this will raise an error because the set no longer exists



#                                           --JOIN SETS--



#There are several ways to join two or more sets in Python.

#You can use the union() method that returns a new set containing all items from both sets, 
#or the update() method that inserts all the items from one set into another:
#The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)#1, 'c', 2, 3, 'a', 'b'}

#The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)#{1, 'c', 2, 'b', 'a', 3}

#Keep ONLY the Duplicates

#The intersection_update() method will keep only the items that are present in both sets.
#Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)#{'apple'}
print(y)#{'google', 'apple', 'microsoft'}

#The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)#{'apple'}




#Keep All, But NOT the Duplicates



#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)#{'google', 'banana', 'microsoft', 'cherry'}

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)#{'google', 'banana', 'microsoft', 'cherry'}


#                                         --SET METHODS--



#Set Difference:
#The Set type has a difference() method that returns the difference between two or more sets:
#The difference between the two sets results in a new set that has elements from the first set which aren’t present in the second set.
#In Python, you can use the set difference() method or set difference operator (-) to find the difference between sets.

s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.difference(s2)

print(s)#{'Python'}


s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s2.difference(s1)

print(s)#{'C#'}


s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1 - s2

print(s)#{'Python'}


s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s2 - s1

print(s)#{'C#'}

#The set difference() method can accept one or more iterables 
# (e.g., strings, lists, dictionaries) while the set difference operator (-) only allows sets.

#The following shows how to use the set difference() method with a list:

scores = {7, 8, 9}
numbers = [9, 10]
new_scores = scores.difference(numbers)

print(new_scores)#{8,7}

#However, if you use the set difference operator (-) with iterables, you’ll get an error


#Symmetric Differences

#The symmetric difference of two sets is a set of elements that are in either set, but not in their intersection.
#The Set type has the symmetric_difference() method that returns the symmetric difference of two or more sets:

s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.symmetric_difference(s2)
print(s)#{'C#', 'Python'}

#Using the symmetric difference operator(^) to find the symmetric difference of sets

s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1 ^ s2
print(s)#{'Python', 'C#'}


#The symmetric_difference() method accepts one or more iterables that can be strings, lists, or dictionaries.

scores = {7, 8, 9}
ratings = [8, 9, 10]
new_set = scores.symmetric_difference(ratings)
print(new_set)#{10, 7}

#However, the symmetric difference operator (^) only applies to sets. 
# If you use it with the iterables which aren’t sets, you’ll get an error.



#Subset in Sets


#Suppose that you have two sets A and B. The set A is a subset of the set B if all elements of A are also elements of B.
#Then, the set B is a superset of the set A.
#In Python, you can use the Set issubset() method to check if a set is a subset of another:

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
print(scores.issubset(numbers))#True

#By definition, a set is also a subset of itself. The following example returns True:

numbers = {1, 2, 3, 4, 5}
print(numbers.issubset(numbers))#True

#The following example returns True because some elements in the numbers set aren’t in the scores set. 
# In other words, the numbers set is not a subset of the scores set:

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
print(numbers.issubset(scores))#False

#Besides using the issubset() method, you can use subset operators (<=) to check if a set is a subset of another set:
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = scores <= numbers
print(result)  # True

result = numbers <= numbers
print(result)  # True


#The proper subset operator (<) check if the set_a is a proper subset of the set_b:

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = scores < numbers
print(result)  # True
#In this example, the set numbers are not a proper subset of itself, therefore, the < operator returns False.
result = numbers < numbers
print(result)  # False

#Suppose that you have two sets: A and B. 
#The set A is a superset of the set B if all elements of the set B are elements of the set A

#If the set A is a superset of the set B, then the set B is a subset of the set A.
#  To check if a set is a subset of another, you use the issubset() method.

#If the set A and set B are not equal, the set A is a proper superset of the set B.
#Logically, a set is a superset of itself.
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
result = numbers.issuperset(scores)
print(result)#True

numbers = {1, 2, 3, 4, 5}
result = numbers.issuperset(numbers)
print(result)#True


numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
result = scores.issuperset(numbers)
print(result)#False


#The >= operator determines if a set is a superset of another set:

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = numbers >= scores
print(result)  # True

result = numbers >= numbers
print(result)  # True


#To check if a set is a proper superset of another set, you use the > operator:

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = numbers > scores
print(result)  # True

result = numbers > numbers
print(result)  # False


#If the values of two different variables are equal it will also be superset of var1
numbers = {1, 2, 3}
scores = {1, 2, 3}
result = numbers.issuperset(scores)
print(result)#True



#Disjoint Sets


#Two sets are disjoint when they have no elements in common. 
#In other words, two disjoint sets are sets whose intersection is an empty set.

odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}
result = odd_numbers.isdisjoint(even_numbers)
print(result)#True

letters = {'A', 'B', 'C'}
alphanumerics = {'A', 1, 2}

result = letters.isdisjoint(alphanumerics)

print(result)#False

#The following example passes a list to the isdisjoint() method instead of a set:

letters = {'A', 'B', 'C'}
result = letters.isdisjoint([1, 2, 3])
print(result)#True



#                                       --SET COMPREHENSION--








