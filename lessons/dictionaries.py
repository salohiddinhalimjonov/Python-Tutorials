#                                    --DICTIONARIES--



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#Dictionaries are written with curly brackets, and have keys and values:


#You can access the items of a dictionary by referring to its key name, inside square brackets:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)#Mustang

#There is also a method called get() that will give you the same result:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)#Mustang

#The keys() method will return a list of all the keys in the dictionary.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)#dict_keys(['brand', 'model', 'year'])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
#result:
#dict_keys(['brand', 'model', 'year'])
#dict_keys(['brand', 'model', 'year', 'color'])


#The values() method will return a list of all the values in the dictionary.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)#dict_values(['Ford', 'Mustang', 1964])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
#dict_values(['Ford', 'Mustang', 1964])
#dict_values(['Ford', 'Mustang', 1964, 'red'])

#The items() method will return each item in a dictionary, as tuples in a list.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")#Yes, 'model' is one of the keys in the thisdict dictionary


#                                      --CHANGE LIST ITEMS--



thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}


#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}



#                                  --ADD ITEMS--



#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}



#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

#The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


#There are several methods to remove items from a dictionary:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)#{'brand': 'Ford', 'year': 1964}

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)#{'brand': 'Ford', 'model': 'Mustang'}

#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)#{'brand': 'Ford', 'year': 1964}

#The del keyword can also delete the dictionary completely:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

#The clear() method empties the dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)#{}



#                                    --LOOP DICTIONARIES--


#You can loop through a dictionary by using a for loop.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
#brand
#model
#year

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
#Ford
#Mustang
#1964

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
#Ford
#Mustang
#1964

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
#brand
#model
#year

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
#brand Ford
#model Mustang
#year 1964

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


#                                     --COPY DICTIONARIES--



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
mydict.pop('model')
print(mydict)
print(thisdict)
#results
#{'brand': 'Ford', 'year': 1964}
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}



#                             --NESTED DICTIONARIES--



child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)#result:
#{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}


#                                           --DICTIONARY METHODS--



#The fromkeys() method returns a dictionary with the specified keys and the specified value.

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)#['key1': 0, 'key2': 0, 'key3': 0]



x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)#['key1': None, 'key2': None, 'key3': None]



car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "White")
print(x)#White
print(car)#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)
print(car)
#results:
#Mustang
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


#Reminder:
#dictionary.setdefault(keyname, value)
#Parameter Values
#Parameter	Description
#keyname	Required. The keyname of the item you want to return the value from
#value	Optional.
#If the key exist, this parameter has no effect.
#If the key does not exist, this value becomes the key's value
#Default value None



#                                       --DICTIONARY COMPREHENSION--



