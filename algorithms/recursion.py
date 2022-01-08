#Tasavvur qilamiz, Bitta katta sandiq bor va uni ichida bir nechta qutilar bor. 
#Qutilarning ichida yana qutilar bo'lishi mumkin
# va ularning birida kalit bor va biz ushbu kalitni topishimiz kerak

#1.Qutilarni bir joyga jamlaymiz 
#2.Toki to'plamda qutilar bor ekan
#3.Bitta qutini ochamiz
#4. Agar qutida boshqa quti bo'lsa, to'plamga qo'shamiz
#5.va 2-qadamga qaytamiz
#6. Agar 3-bosqichdan keyin kalitni topsak, qidirishni to'xtatamiz.

#Recursive funksiyalar ikki qismdan iborat bo'ladi:
#1. Rekursiya sharti(recursive case)
#2.To'xtash sharti(base case)
#Example:
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)#Recursion
        elif item.is_a_key():
            print("Found the key!")    

#Another example
def sana(n):
    print(n)
    if n<=1:
        return
    else: 
        sana(n-1)
sana(10)

#Another Example:
def fact(x):
    if x==1:
        return 1
    else:
        return x * fact(x-1)    

        