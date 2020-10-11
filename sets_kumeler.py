
k1 = {10, 20, 30, 40}
k2 = { 30, 40, 50, 60, 70}
print(k1|k2)   #iki kümeyi birleştirir, birleşim işlemi set union
print(k1-k2)   #kume farkı, ifade oncelıgı var. k1 de olan ancak k2 de olmayana elemanları alır
print(k1&k2)   #kesişim islemi. İki kümenin kesişimini alır
print(k1^k2)   #exculesive or, özel veya hem k1 de olup k2 de olmayanlar, veya k2 de olan k1 de olmayanları bastırır

#Ayrıca kümeler asagıdaki gibi tanımlanabilir
#k5 = set([5,3,6])
#k6 = set("merhaba")
#print(k5, k6)
# kume = {0,1,2,3,2,1,3,21,2,3,1}  #küme tekrar eden ifadelerden sadece 1 tanesını alır
#print(kume)