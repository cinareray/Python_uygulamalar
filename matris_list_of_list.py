#list of list
l1 =[[[10, 20], [30, 40, 50]], [[  [[60, 70, 80], ["Eray"]], ["cinar"], [2, 7, 8]]], ["Sivas"]  ]
print(l1[1])


l2=list(map(lambda x:x+4, range(4)))
print(l2)
l3=[(i+i+2) for i in range(1,4) ]
print(l3)
l4=[l2, l3, ["eray", "cinar", 58]]
print(l4)
#matrisin transpozesini alma (döndürme)
l4_transpoze = [[satir[i] for satir in l4] for i in range(3)]  #satir dizisi yardımcı oldu ve silindi
print(l4_transpoze)

print(list(zip(*l4)))    #zip operatörü otomatik olarak transpoze alır.
