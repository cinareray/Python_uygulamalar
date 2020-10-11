def merhaba():      #parametresiz fonksiyonlar...
    print("merhaba ")
def fak(f):         #varsayılan parametre atanması(DEFOULT PARAMETER)
    sonuc=1;
    for a in range(1,f+1):
        sonuc  = sonuc * a
    return sonuc
def fakto(f):          #özyineli fonksiyonlar (recursive functions)
    if(f==0): return 1
    return f*fakto(f-1)
def topla(*a):          #esnek eleman demektir.  "a" artık bir dizi şeklindedir.
    sonuc = 0
    for i in a:
        sonuc = i + sonuc
    return sonuc
def fucntion(**a): #dictionary dizisi yaratır.
   for i in a:
        print(str(i) , str(a[i]))  # str(i) keysler....str(a[i]) ise valuable 




def main():
    #merhaba("eray")
    #print(fak(5))
    #print(fakto(6))
    #print(topla(1,23,2,4))
    fucntion(eray=58,cinar=34,a=4,b=5)
if __name__ == '__main__':
    main()
