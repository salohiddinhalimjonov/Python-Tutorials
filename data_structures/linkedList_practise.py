class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next    
    
    def push(self,new_data):
        """List boshiga tugun qo'shish"""
        #yangi node ochamiz
        new_node = Node(new_data)
        #List boshini keyingi o'ringa suramiz
        new_node.next = self.head
        #Yangi nodeni list boshiga qo'yamiz
        self.head = new_node

    def insertAfter(self, prevnode, new_data):
        if not prevnode:
            print("Bunday tugun mavjud emas!")
        new_node = Node(new_data)
        #O'rnatmoqchi bo'lgan tugunimizning manziliga undan avval turishi 
        #kerak bo'lgan tugundan keyin turgan tugunning manzilini yuklaymiz
        #chunki yangi tugun ikki tugunning orasiga qo'shilyapti va undan keyingi tugunni
        #manzilini saqlashi kerak.
        new_node.next = prevnode.next
        #O'rnatmoqchi bo'lgan tugunimizdan avval turgan tugun saqlayotgan manzil
        #endi yangi tugundan keyingi tugunning manzilidir. Shuning uchun uni
        #yangi tugunning manziliga o'zgartiramiz.
        prevnode.next = new_node    
    
    def append(self,new_data):
        node = Node(new_data)
        if self.head is None:
            self.head = node
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def deleteNode(self,key):
        """Listdan qiymat o'chirish"""
        #List boshini topib olamiz
        temp = self.head
        #Birinchi tugunni tekshiramiz
        if (temp and temp.data==key):
            self.head = temp.next  
            temp = None
            return
        #Aks holda keyingi tugunlarni qarab chiqamiz
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next 
        #Agar qiymat topilmasa
        if temp == None:
            return
        #Tugunni listdan o'chiramiz
        prev.next = temp.next
        temp=None
                
