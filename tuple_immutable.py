# tuplle yapısını lamba_map_side_effect.py orneginde işlemiştik. immutable(değiştirilemez)
l1 = (10, 20, 30)  #tuple tanımlanması l1 = 10, 20, 30 da olanilir parantezsiz
                   #listelerden farkı [] ların yerine () kullanılması ve tuple ların değiştirilemez yani immutable olması
print(l1)
#l1[0] = 50         #hata verecektir.

l2 = [0, 1, 2]
print(l2)           #listeler mutable(değiştirilebilirdir)
l2[0]=90
print(l2)

#tuple'nın bir elemanını değiştirmek için yeni tuple gereklidir.
t = ("eray", "cinar", 58)
print("İlk tuple : ", t)
x, y, z = t               #unpacking (paket açma ) denilir
y = 34
t=(x, y, z)
print("Son tuple" , t)