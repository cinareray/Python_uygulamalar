
def whiledongusu():
#fibonacci serisi
    a, b= 0,1  # a=0 , b=1 demektir.
    while a<30:
        a,b=b,a+b  # a=b , b=a+b demektir.
        print(a)   # ekrana a yaz.

def fordongusu():
    liste1 = [ "ahmet" , 1, 2, 3, "mehmet"]
    #for i in liste1:    # i yi dongu üzerinde donmesı...
        #print(i)
    #for i in range(0,100):      #range aslında bir liste oluşturur. Başlangıc noktası 0 son nokta 100 birer birer artar...
        #print(i)
    for i in range(0,20):
      if(i%3==0):
         continue   # continue anlamı eger bu komut gorulur ise dongunun basına gider...
      print(i)
    for i in range(1,20):
       if(i%3==0):
          break   # donguyu sonlandırır.
       print(i)
    for i in range(5,20):
        pass           #boş dongu demektir.,,,,,,,,,,ü
def main():
    fordongusu()

if __name__ == '__main__':
    main()