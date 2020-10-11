#Foksiyonel programlamada fonksiyonlar ön plandadır. Yapılacak bir uygulama hem OOP hemde Fonksiyonel programlama ile
# de yapılabilir. Fonssiyonel programlama kullanıcı tarafından daha esnek ve daha anlaşılır bir kodlamadır.
# fonksiyonel programlamayaı üç özellik üzerinden incelenebilir..
#yan etkisiz fonksiyonlar(Pure functions) : birbirinden bagımsız fonksiyonlar girdi-çıktı ilişkisi
# yüksek seviye fonksiyonlar , İsimsiz fonksiyonlar (Anonymous functions):  lambda yapısı
# vektorel operasyonlar (numpy kütüphanesini kullanarak ikidiziyi vektorel olarak carpma ) :
# map , filter , reduce ifadeleri vektorel operasyonlardır.

#PURE FONCTION :
#OOP
class fitness():
    def __init__(self):
        self.name = ""
        self.lastname = ""
    def yazma(self):
        self.name = "merhaba"
    def okuma(self):
        return len(self.name)

a = fitness()
print("basta", a.name, a.okuma())
a.yazma()
# sadece yazma fonksiyonu calıştırıldığında okuma fonksiyonun degerıde degısmektedir. Buna ölümcül etki olarak isimlendirilir.
print("yazma fonksiyonu calistiridiktan sonra : ", a.name, a.okuma())

#FP: görüldüğü üzere girdi vermeden cıktı uretmeyen fonksiyonlar
def write(yazi):
    return yazi
def read(hi):
    return len(hi)
example = write("merhaba")
example_read = read(example)
print(example_read)

#isimsiz fonksiyonlar
#OOP ile oluşturulan:

liste1 =[0, 1,2,3]

# asagıda olusturula i degeri hala bellekte bulunmaktadır.
for i in liste1:
    print(i+10)
# yuksek seviyeli fonksiyonlar : map ve lambda
liste11= list(map(lambda x: x + 10, liste1))  # x artık bellekte bulunmamaktadır.
print(liste11)

#filter kullanımı koşul sorularını yazabiliriz.
liste3 = [0,1, 2, 3, 6, 8,10,15,45,21,36]
liste4 = list(filter(lambda x: x > 15, liste3))
print(sorted(liste4))

#reduce  bnedeyokanalmadım ??
liste5 = [1, 2, 3, 4]
#reduce(lambda a,b: a+b, liste5)
