#Syntax Error - dasturlash qoidalariga amal qilmaslik natijasida 
#kelib chiqadi. Misol uchun:
# print "Hello World!" 
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World!")?

#EOL (End of line) va EOF xatolik - sintaks xatolikning bir turi bo'lib, oddatda qator oxirida
#qo'shtirnoqni yopish esdan chiqqanda yuzaga keladi. Misol uchun:
#print("Hello World!
#SyntaxError: EOL while scanning string literal
# EOF (End of function) xatoligi funksiya oxirida qavsni yopish esdan
#chiqqanda yuzaga keladi. Misol uchun:
#print("Hello World!"
#SyntaxError: unexpected EOF while parsing

#Indentation Error - Joy tashlashdagi xatolik. Misol uchun:
#for n in range(10):
#print(n+1)
#IndentationError: expected an indented block

#Runtime Error - dasturni bajarishda kelib chiqadi va dasturning ishlashini to'xtatadi
#Sintaks xatolikdan farqli ravishda Python bunday xatolarni dasturni bajarishdan avval aniqlay olmaydi.
#Runtime Errorning bir nechta turlari bor.

#Type Error - Biror amalni(funksiya, metod) noto'g'ri ma'lumot ustida bajarish.
#son = input("Istalgan son kiriting: ")
#print(f"{son} ning kvadrati {son**2} ga teng")
#TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

#Name Error - o'zgaruvchi, funksiya, obyekt nomini noto'g'ri yozish natijasida kelib chiquvchi xatolik.
#mevalar = ['olma','uzum','nok','anor','anjir']
#for meva in mvealar:
#    print(meva)
#NameError: name 'mvealar' is not defined

#prit("Hello World!")
#NameError: name 'prit' is not defined

#Value Error - Funksiyaga noto'g'ri qiymatni yuborish natijasidagi xatolik
#son = int(input("Istalgan son kiriting: "))
#if son>=0:
#    print("Musbat son")
#else:
#    print("Manfiy son")
#Value Error - agar float number kiritilsa, misol uchun 4.5

#Index Error - ro'yhatdagi maksimum index raqam biz kiritgan index raqamdan kichik bo'lsa
#ushbu hatolik yuzaga keladi.
#mevalar = ['olma','anor','uzum']
#print(mevalar[3])
#IndexError: list index out of range

#ZeroSivisionError - dastur davomida 0ga bo'lish yuzaga kelgandagi xatolik
#x,y = 50,50
#z = 250/(x-y)
#ZeroDivisionError: division by zero