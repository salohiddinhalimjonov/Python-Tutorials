from linkedList_practise import Node, LinkedList

llist = LinkedList()
llist.head = Node("Dushanba")
tuesday = Node("Seshanba")
wednesday = Node("Chorshanba")
llist.head.next = tuesday#Bu yerda bosh tugunning nextiga keyingi tugunning
#manzilini saqlayapmiz
llist.head.next.next = wednesday
print(llist.head.next.next.data)
llist.push("Yakshanba")
llist.insertAfter(llist.head.next, "Juma")
llist.append("Payshanba")
llist.deleteNode("Yakshanba")
llist.printlist()