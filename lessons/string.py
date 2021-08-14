#                                         --STRING--



#Strings in python are surrounded by either single quotation marks, or double quotation marks.
#'hello' is the same as "hello".
#You can display a string literal with the print() function:
print("Hello")#Hello
print('Hello')#Hello
#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)#Hello

#You can assign a multiline string to a variable by using three quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#result : 
#Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.

#Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
#However, Python does not have a character data type, a single character is simply a string with a length of 1.
#Square brackets can be used to access elements of the string.
a = "Hello, World!"
print(a[1])#e
 
#Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
      print(x) #b
               #a
               #n
               #a
               #n
               #a
#To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))#13

#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)#True

#Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)#True

#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])#llo
a = [1,2,3,4,5,6,7]
print(a[5:2:-1])#result: ,ol

#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age
#But we can combine strings and numbers by using the format() method!
#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))#I want 3 pieces of item 567 for 49.95 dollars.

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))#I want to pay 49.95 dollars for 3 pieces of item 567



#Or we can combine them in this way:
print(f"I want to pay {price} dollars for {quantity} pieces of item {itemno}.") 



#                           --ESCAPE CHARACTERS--



txt = "We are the so-called \"Vikings\" from the north."
print(txt)#We are the so-called "Vikings" from the north.

txt = 'It\'s alright.'
print(txt)#It's alright.

txt = "This will insert one \\ (backslash)."
print(txt)#This will insert one \ (backslash).

txt = "Hello\nWorld! Hello\nmy"
print(txt)#Hello
          #World!
          #Hello
          #my

txt = "Hello\tWorld!"
print(txt)# Hello World!

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)#HelloWorld!

txt = "Hello\rWorld\r!"
print(txt)#Hello
          #World
          #!



#                                 --STRING METHODS--



#capitalize()	Converts the first character to upper case
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)#Hello, and welcome to my world.
#casefold()	Converts string into lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)#hello, and welcome to my world!
#center()	Returns a centered string
txt = "banana"
print(txt.center(20))#       banana
txt = "banana"
x = txt.center(20, "O")
print(x)#OOOOOOObananaOOOOOOO

#count()	Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)#2

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10,     20)#it calculates the count of the given value in the txt between the given range of indexes
print(x)               #start   end 
                       #index   index
# result is 1                       

#encode()	Returns an encoded version of the string

#endswith()	Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)#True
#string.endswith(value, start, end)
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)#False
#expandtabs()	Sets the tab size of the string
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(8)
print(x)#H       e       l       l       o

#find()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)#7
#Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 20)
print(x)#8
#format()	Formats specified values in a string
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "<" to left-align the value:

txt = "We have {:<8} chickens."
print(txt.format(49))
#We have 49       chickens.

#format_map()	Formats specified values in a string


#index()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)#8
#isalnum()	Returns True if all characters in the string are alphanumeric
#The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
txt = "Company12"
x = txt.isalnum()
print(x)#True

txt = "Company 12"
x = txt.isalnum()
print(x)#False
#isalpha()	Returns True if all characters in the string are in the alphabet
txt = "CompanyX1"
x = txt.isalpha()
print(x)#False

txt = "CompanyX"
x = txt.isalpha()
print(x)#True
#isdecimal()	Returns True if all characters in the string are decimals
#The isdecimal() method returns True if all the characters are decimals (0-9).
#This method is used on unicode objects.
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())#True
print(b.isdecimal())#False

#isdigit()	Returns True if all characters in the string are digits
txt = "50800"
x = txt.isdigit()
print(x)#True
#isidentifier()	Returns True if the string is an identifier
#The isidentifier() method returns True if the string is a valid identifier, otherwise False.
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
#A valid identifier cannot start with a number, or contain any spaces.
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())#True
print(b.isidentifier())#True
print(c.isidentifier())#False
print(d.isidentifier())#False

#islower()	Returns True if all characters in the string are lower case
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())#False
print(b.islower())#True
print(c.islower())#False
#isnumeric()	Returns True if all characters in the string are numeric
#The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
#Exponents, like ² and ¾ are also considered to be numeric values.
#"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
txt = "565543"
x = txt.isnumeric()
print(x)#True



a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"
f = "1234"

print(a.isnumeric())#True
print(b.isnumeric())#True
print(c.isnumeric())#False
print(d.isnumeric())#False
print(e.isnumeric())#False
print(f.isnumeric())#True

#isprintable()	Returns True if all characters in the string are printable
#The isprintable() method returns True if all the characters are printable, otherwise False.
#Example of none printable character can be carriage return and line feed.
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)#True

txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)#False
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()	Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning

 




