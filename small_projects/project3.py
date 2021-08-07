import random
def son_top(x = 10):
    tasodifiy = random.randint(0,x)
    print(f'Men 0dan {x}gacha oraliqda bir son o\'yladim. Siz uni topa olasizmi?')
    taxminlar =0
    while True:
        taxminlar += 1
        respond = int(input('Tahminingizni kiriting : '))
        if respond > tasodifiy:
            print('Xato! Men o\'ylagan son bundan kichikroq. Yana harakat qilib ko\'ring : ')
        elif respond < tasodifiy:
            print('Xato! Men o\'ylagan son bundan kattaroq. Yana harakat qilib ko\'ring : ')
        else:  
            break
    print(f'To\'g\'ri. Siz {taxminlar}ta taxmin bilan to\'g\'ri javobni topdingiz! ')    
    return taxminlar


def sen_top(x = 10):
    input(f' Endi siz 0 va {x} oralig\'ida bir son o\'ylang, men uni topaman. O\'yinni boshlash uchun biror tugmani bosing : ')
    bosh = 0
    oxir = x
    taxmini = 0
    while True:
        taxmini += 1
        if bosh != oxir:
            taxminim = random.randint(bosh,x)
        else:
            taxminim = bosh
        javob = input(f'Siz {taxminim} degan sonni o\'yladiz : Tahminingiz to\'g\'ri(T), Tahminingiz kichikroq(-), Tahminingiz kattaroq(+) :')
        if javob == '-':
            bosh = taxminim + 1
        elif javob == '+':
            oxir = taxminim - 1
        else :
            break
    print(f'Men {taxmini}ta tahmin bilan to\'g\'ri javobni topdim.')    
    return taxmini

def play(x = 10):
    funct1 = son_top(x)
    funct2 = sen_top(x)
    while True:
      
        if funct1 < funct2:
            print('Siz yutdingiz !')
        elif funct1 > funct2:
            print('Men yutdim')  
        else:
            print('Durang')
        yana = input('Yana o\'ynaysizmi (ha/yo\'q)?')
        if yana == 'ha':
            play()
           
        else:
            break    
play()        





     