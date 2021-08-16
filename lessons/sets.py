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












