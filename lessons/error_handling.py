#Runtime Errorlarni oldini olish uchun pythonda exceptionlardan foydalanamiz.
#try-except: try operatori - ushbu qismga bajarish kerak bo'lgan kod yoziladi
# except operator - ushbu qismga xatolik yuzaga kelganda bajarilishi kerak bo'lgan
#kod yoziladi.
#Misol uchun:
#yosh = input("yoshingizni kiriting: ")
#yosh = int(yosh)
#print(f"Sizning yoshingiz {yosh}da")
#Agar foydalanuvchi yoshini kiritayotganda o'nli son kiritsa Value Error
#xatoligi sodir bo'ladi.
#Buni try-except yordamida oldini olamiz:
yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)
    print(f"Sizning yoshingiz {yosh}da")
except:
    print("Butun son kiritmadingiz")    
print("Dastur tugadi!")    
