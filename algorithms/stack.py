#Stack:
#LIFO(Last In First Out) - Oxirgi kirgan, birinchi chiqadi
#Ma'lumotlar to'plam ustiga qo'shiladi va to'plam ustidan olinadi
#Misol uchun: email pochtaga kelgan eng oxirgi habar, eng avval ko'rinadi

#Stack ustida amallar:
#Push - element qo'shish
#Pop - element sug'urib olish
#isEmpty - to'plam bo'sh ekanligini tekshirib ko'rish
#isFull - to'plam to'la ekanligini tekshirish
#Peek - eng yuqoridagi element qiymatini ko'rish

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack)==0

    def push(self, data):
        self.stack.append(data)    
        return "Done!"

    def pop(self):
        if self.isEmpty():
            print("No data inside stack")
        else:
            return self.stack.pop()
            

    def peek(self):
        """Eng ustki elementni ko'rish"""
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]   
stack1 = Stack()
print(stack1.push("Hello"))
print(stack1.peek())



#Rekursiv funksiyalar ham stack asosida ishlaydi
#Dasturlashda bu call stack yoki program stack deyiladi
#Misol uchun:
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)    

fact1 = fact(5)#5dan paski raqamlarga qarab hisoblayapti, yani oxirgisi birinchida



