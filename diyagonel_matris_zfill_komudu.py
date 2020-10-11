sayi=int(input("Bir sayı giriniz:"))
for i in range(0,sayi):
    ekran = str(10**i).zfill(sayi)[::-1]  #z.fill ekrana yazılan stringin sol tarafına 0 ekler
    print(ekran)

zf="Merhaba"              # merhaba yazısı 7 karaterdir ve ekranda görüldüğü üzere sol tarafına 0 konulacaktır.
print(zf.zfill(8))
print(zf.zfill(20))
print(zf.zfill(5))