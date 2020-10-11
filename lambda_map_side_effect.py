#side effect oluşumu döngüler ile yapılmada oluşmakta.
#Amaç 1-10 a kadar olan sayıların karelerini barındıran bir liste oluşturmak...
l1 =[]
for x in range(1,11):
    l1.append(x**2)
print(l1)
print(x)    #Liste oluşturuldu ancak istenmeyen bir değişken hafızada kaldı. Buna Side effect(yan etki) denilir.
            #her kodun bir amacı vardır ve amacın dısında başka bir işlem yapılmaması istenir. Yapılır ise buna Side effect denir.

#Eğer side effect olmadan amacımıza ulaşmak istersek
l2 = list(map(lambda a: a**2, range(1,11)))    # list("içindeki yapıyı listeye cevirir")
                                               #map ise bir fonksiyonu al bütün listenin bütün elemanlarına uygula anlamına gelir.
                                               #map bir işi parçalayıp ayrı ayrı bilgisayarlara dağıtarak tek bir işi yapmalarını
                                               #sağlaması için kullanılır. Big date uygulamalarında sıkça kullanılır...
                                               #lambda function pointer(isimsiz fonksiyonlar) boşluğu ifade eder..

print(l2)
#print(a)   bakıldığında hata olacaktır çünkü oluşturulan parametre kullanıldı ve silini ayrıca ortada bir fonksiyonda
#kalmayacaktır. Ortada sadece 1-10 a kadar olan sayıların kareleri olan listemiz kalacaktır...

print("Tuple yapısı :")
liste6= [(p**2) for p in range(4)]   #tuple yapısı olarak geçmektedir
print("Liste6 = ",liste6)            #Aynı şekilde p operatörü amac sonunda silinecektir.

liste7=[(p, l) for p in [0,5,3] for l in [5,8,2] if p!=l]  #çıkan sonuç incelenmelidir.
print("liste7 : ", liste7)


def f(k):
    return k+5
def main():
 l4=[1,2,3]
 l5=list(map(f,l4))   # f fonksiyonunu l4 listesindeki her eleman için uygula MAP kavramını açıklanabilir.
                      # map in ilk parametresi bir fonksiyondur ikici parametre ise listedir
 print(l5)

if __name__ == '__main__':
    main()