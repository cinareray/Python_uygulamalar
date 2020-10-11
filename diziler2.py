def kopyalama():
 #shallow copy (sığ kopyalama)
 a =[ "eray" , "cinar",500 ]
 d=a
 print(a , d)  # a de ye shallow copy kopyalandı. a ile d nin adreslendiği alan aynı yerdedir bu yüzden ...
 a[0] = "halil"
 print ( a , d )  # shallow copy'de kopyalama ile a da yapılan bir değişiklik d'de görülecektir

#deep copy (derin kopyalama)
 c=a[:]   #a'nın elemanlarını c'ye kopyala  hafızada artık a ile c ayrı yerlerde adreslendı
 a[0]= "nadire"   #a'da yapılan bir değişiklik c'ye yansımayacaktır.
 print (a , d , c)
 c[0] = "mutlu"  #aynı sekılde c'de yapılan bir değişiklik a'ya yansımayacaktır.
 print (a , d , c)
def dizi_eleman_ekle():
 #diziye eleman ekleme
 c.append("05386840469")   #listelerde bu terim yeterlidir ancak stringlerde c = c.append("selam") ' dememiz dogru olur.
 print (c)
def siralama():
# sort komutu buyukten kucuge dogru sılanması demektir
 k = [ "eray" , "nadire","mutlu" , "halil" ,"ahmet"]
 k.sort()
 print(k)
 a=[45,132,54,123,65,8,42,25,1]
 a.sort()
 print (a)

def in_komutu():
    b = [ 0 ,1,2,3,58,67,34]
    for i in b:   # i değişkeni  b içerisinde 0'ıncı elemandan baslıyarak dolasacak anlamına gelmektedir.
        print (i)
def main():
    siralama()

if __name__ == '__main__':
    main()



