def birinci():
    f=open("deneme.txt","w")    #w dosya acar ve içerisine yazar
    f.write("merhaba")
    f.close()
    f=open("deneme.txt","r")   #sadece dosya okumak içindir.
    print(f.read())
    f.close()
    f=open("deneme.txt", "a")  # var olan dosya üzerine ekler yazar.
    f.write("\na da yazmak")
    f.close()
    f=open("deneme.txt","r+")  #r+ hem yazma hem okuma işlemlerini görür ancak burda olmadı
    print(f.read())
    f.close()
def ikinci():
    f=open( "deneme_bir.txt", "a")
    f.write("Deneme1 r+ da yazmak")
#    print(f.read())
    f.close()

def main():
    ikinci()
if __name__=="__main__":
    main()