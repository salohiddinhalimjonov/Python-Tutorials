#                                          --CLASSES--



#The first argument of every class method, including init, is always a reference to the current instance of the class.
#By convention, this argument is always named self. In the init method, self refers to the newly created object; in other class methods, it refers to the instance whose method was called.

#Python doesn't force you on using "self". You can give it any name you want.
#But remember the first argument in a method definition is a reference to the object. Python adds the self argument to the list for you; you do not need to include it when you call the methods. if you didn't provide self in init method then you will get an error

#TypeError: __init___() takes no arguments (1 given)
#What does the init method do? Why is it necessary? (etc.)

#init is short for initialization. 
# It is a constructor which gets called when you make an instance of the class and it is not necessary. 
# But usually it our practice to write init method for setting default state of the object.
#If you are not willing to set any state of the object initially then you don't need to write this method.

class User:
    def __init__(self, username, firstname, lastname, email, password):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def get_info(self):
        return f"I am {self.firstname}"    

object1 = User('001', 'salohiddin', 'halimjonov', '00009998id@gmail.com', '123456')        
print(object1.get_info())