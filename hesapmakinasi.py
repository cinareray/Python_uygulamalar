def main():
    print("Hesap makinasina hosgeldiniz...")
    secim = int(input(print("Yapmak istediğiniz işlemi seçin :\n1)Toplama \n2)Çıkarma \n3)Çarpma \n4)Bölme ")))
    if secim==1:
        toplama()
    if secim==2:
        cikarma()
    if secim==3:
        carpma()
    if secim==4:
        bolme()
def toplama():
    sayilar=[]
    sonuc=0
    while 1:
        x=float(input("Sayı girin (bitirmek için -9.9): "))
        if x==-9.9:
            break
        sayilar.append(x)
    for i in sayilar:
        sonuc=sonuc + i
    print(sayilar)
    print("Sonuc :" ,sonuc)

def cikarma():
    sayilar=[]
    sonuc = 0
    while 1:      #sonsuz döngü
        x=float(input("Sayı girin(bitirmek için -9.9)"))
        if x==-9.9:
            break
        sayilar.append(x)
        sonuc += x
    print(sayilar)
    print("Sonuc: ", sonuc)

def carpma():
    sayilar=[]
    sonuc=1
    while 1:
        x=float(input("Sayı girin(Bitirmek için -9.9"))
        if x==-9.9:
            break
        sayilar.append(x)
        sonuc=sonuc*x
    print(sayilar)
    print("Sonuc:", sonuc)

def bolme():
    sayilar=[]
    sonuc=1
    for i in range(0,2):
        x=float(input("Sayı girin: "))
        sayilar.append(x)
    sonuc = sayilar[0]/sayilar[1]
    print(sonuc)

if __name__ == '__main__':
    main()