#Tracker - 20000
#Spark - 8000
#Ravon R2 - 9000
#Cobalt - 10000
#Malibu - 32000
#Lacetti - 12000
#Tahoe - 63000
#Traverse - 55000
#Yuqorida ko'rsatilgan ushbu ro'yhatni quyidagi tartibga keltirish
#uchun:
#Tahoe - 63000
#Traverse - 55000
#Malibu - 32000
#Tracker - 20000
#Lacetti - 12000
#Cobalt - 10000
#Ravon R2 - 9000
#Spark - 8000

#Birinchi qiladigan ishimiz:
#1.Bo'sh ro'yhat yaratamiz
#2.Betartib ro'yhat ichidan eng katta qiymatga egasini topib (Linear Search algoritmi orqali) bo'sh ro'yhat
#tomonga o'tkazamiz
#3.Shu tarzda qolgan elementlarning eng ham eng kattasini topib bo'sh ro'yhat tomonga
#o'tkazaveramiz. 
def selectionSort(arr):
    new_arr = []
    if not arr:
        print("No data inside array!")
    while arr:
        max_number = arr[0]
        for num in arr:
            if max_number >= num:
                max_number = num
        new_arr.append(max_number)
        
        arr.remove(max_number)
        
    return new_arr

SelectionSort = selectionSort([5,6,2,4,8])
print(SelectionSort)#[2,4,5,6,8]