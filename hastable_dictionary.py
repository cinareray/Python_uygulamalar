#hastable yada dictionary kavramları
#dinamik hafıza söz konusu
#verilere hızlı erişmek için kullanılır.
def dictionary():
    a = {} #a isimli bir sözlük tanımlandı
    a['eray'] = ["cinar" ]        #eray isimli anahtar ve karsılığı olan cinar isimli değer tanımlandı...
    a["hilal"] = ["karadas"]
    a["sivas"] = [58]
    print(a)
    print(a.keys())
    print(a.values())
def sozluk():
    s = { "eray": 58 , "cinar": 34}      #küme parantezi ile dictionary oluşturma
    print(s["eray"])
    s["Zongulda"] = 67          #dictionary eleman ekleme
    print(s["Zongulda"])
    print(s)
    s1 = dict([('sakarya', 54), ('sivas', 58) , ('ankara', 6)]) #dict operatörü ile tanımlama
    print(s1)

    del s1['sakarya']       #eleman silmeye yarar
    print(s1)
    s1['sinop'] = 57
    print(s1['sinop'])

    print('sivas' in s1)        #keys sorgulamak için in kullanılabilir.
    print(sorted(s1))           #sıralama yapar sorted

    s3 = { 'sivas': 58 ,'selam': 10,'merhaba' : 2}
    print(s3)
    print(list(s3))

def loop_tech():
    s3 = {'sivas': 58, 'selam': 10, 'merhaba': 2}
    for anahtar, deg in s3.items():  # items ile anahtarları ve keysler aynı zamanda ekranda görebiliriz
        print(anahtar, ":", deg)
# enumerate ile dizideki elemanların anahtarları ve degerleri ile aynı
# zamanda gösterilebilir. Bilindiği gibi dizilerde bir dict dir her elemanı
# 0,1,2,3 eleman diye isimlendirmekteyiz...
    d1 = ["eray", "cinar", "istanbul"]
    for anahta, deger in enumerate(d1):
        print(anahta,deger)

#Eğer döngü içerisinde iki farklı dizinin elemanlarını aynı anda ekranda görmek istersek
#zip(dizi1,dizi2) şeklinde donguye sokularak ekranda gosterilebilir.
    sorular = ["yaşınız kaç?", "favori renginiz nedir? ","mesleğiniz nedir?" ]
    cevaplar = [ "yaşım 23" , "favori rengim kırmızı", "mesleğim mühendis"]
    for a1, k1 in zip(sorular,cevaplar):
        print("Sizin {0} : Benim {1} " .format(a1,k1))

#dizi elemanlarını tersten yazdırmak istersek reversed komutu bizlere yardımcı olacaktır.
    dizi1 = [ 10, 20, 30, 40, 50]
    for j in reversed(dizi1):
        print(j)
    dizi2 = list(reversed(dizi1))     #dizi1 i ters çevirdik ve dizi2ye liste halınde verdik
    print(dizi2)

#dizileri yada kümeleri büyükten küçüğe yada alfabetik sıralama yapmak istenirse sorted operatörü yardımcı olur
    manav = ["portakal", "elma","şeftali", "limon","armut"]
    for o in sorted(set(manav)):      #alfabetik sıralama yapıldı ve ekrana tek tek yazdırıldı
        print(o)


def main():
   loop_tech()
if __name__ == '__main__':
    main()