def hesapla(a):
    c = a
    if c<100  :           # ":" dan sonra eklenecek bloklar aynı sutun altında olmalıdır..
        print("a ile b'nin çarpımı 100'den kucuktur..."+str(c))
    elif 110<c:
        print("a*b yuz veya 100'den buyuktur",c)
    else:
        print("100-110 arasında")
def main():
    a = int(input("Bir sayı giriniz..."))
    hesapla(a)
## pythonda string yapılası asla degıstırılemezlder cunku constant olarak ele alınırlar....
if __name__ == '__main__':
   main()