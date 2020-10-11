#Kullanıcıdan isims soyisim ve yas alalım ve aldığımız verileri listlerde toplayalım ardından ekrana listeleri bastıralım.

class fitness():

    ad = []
    soyad = []
    yas = []

    def verial():

        fitness.ad.append(str(input("İsminizi giriniz:")))
        fitness.soyad.append(str(input("Soy isminizi giriniz:")))
        fitness.yas.append(int(input("Yaşınızı giriniz: ")))
    def goruntule(i):
        print(" İsim soyisim : ", fitness.ad[i],
              fitness.soyad[i],"\n",
              "Yaşı : ", fitness.yas[i])
def main():
    while 1:
        secim = int(input("1)Yeni kullanıcı\n2)Kullanıcı görüntüle\n3)Tüm kullanıcıları görüntüle\n"
                          "4)Çıkış"))
        if secim==1:
            fitness.verial()
        if secim==2:
            i=int(input("Abone no yu yazınız:"))
            if i==len(fitness.ad):
                fitness.goruntule(i-1)
            else:
                print("Kullanıcı bulunamadı")
        if secim==3:
            toplam = [fitness.ad , fitness.soyad, fitness.yas]
            toplam2 = list(zip(*toplam))
            for i in range(0,len(fitness.ad)):
                print(toplam2[i])
        if secim==4:
            break



if __name__ == '__main__':
    main()

