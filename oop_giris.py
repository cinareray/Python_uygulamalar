class araba:    #araba sınıfı tanımlandı..
    teker =[]     #sınıf özellikleri tanımalacak olan bütün objelerin özelliklerini temsil eder.
    nasil = "SUV"
#self = nesneleri temsil etmektedir. Temsilci olaral adlandırılabilir.
    def __init__(a):   # tanımlacak olan nesnelerin özelliklerini girmek için kullanılır.
        a.marka = []
        a.model =[]

ford=araba()
ford.teker.append("4")
print(ford.teker)
ford.marka="ford"
ford.model= 1972
print(ford.marka , ford.model, ford.nasil)


opel = araba()
opel.marka = "opel "
opel.model = " 2000 "
print(opel.marka, opel.model)
