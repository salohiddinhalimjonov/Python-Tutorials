#                                 --UNPACKING COLLECTION--



fruits = ["apple", "banana", "cherry"]
fruits[0]='peach'
x, y, z = fruits

print(x)#peach
print(y)#banana
print(z)#cherry
print(fruits)#['peach', 'banana', 'cherry']



#                                --OUTPUT VARIABLES--



x = "awesome"
print("Python is " + x)#Python is awesome

x = 5
y = 10
print(x + y)#15

x = 5
y = "John"
print(x + y)#If you try to combine a string and a number, Python will give you an error



#                                  --GLOBAL VARIABLES--



x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()#Python is awesome

#If you create a variable with the same name inside a function, this variable will be local,
#  and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
#result:
#Python is fantastic
#Python is awesome

#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)#Python is fantastic

#Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)#Python is fantastic


#Biror qiymatga nom berganda o'zgaruvchi hosil bo'ladi.O'zgaruchi nomi 1 ta tenglik va qiymat.Namuna: var = 123

#Python dasturlash tilida o'zgaruvchilar turi ko'rsatilmaydi va o'zgaruvchini turini o'zgartirish mumkin.Namuna: a = 3; a = 'anor'; a = False vahokazo.

#O'zgaruvchilar lotin harflari bilan boshlanadi va 2 belgidan keyin ostki chiziq yoki raqamlardan foydalanishingiz mumkin.Namuna: a123, AIR, en_ru

#O'zgaruvchilar nomi birinchi belgisi raqam bilan boshlanishi yoki o'zgaruvchilar nomida simvollar ishtirok etishi mumkin emas.namuna: 123abc, bozor$

#O'zgaruvchilar nomidagi katta va kichik harflar farq qiladi. Narx va narx boshqa boshqa o'zgaruvchi hisoblanadi.