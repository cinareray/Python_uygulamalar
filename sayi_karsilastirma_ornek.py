
def bak(a,b,c):

    if a<b and a>c:    #and ve or olarak kullanılır...
        print("sonuc : c<a<b")
    if b<a and b>c:
        print("Sonuc: c<b<a")
    if c<a and c>b:
        print("Sonuc : b<c<a")
    if c<b and c>a:
        print("Sonuc : a<c<b")
    if b<c and b>a:
        print("Sonuc : a<b<c")
    if a<c and a>b:
        print("Sonuc : b<a<c")


def main():
    a=int(input(print("Birinci Sayıyı giriniz: ")))
    b=int(input(print("İkici sayıyı giriniz: ")))
    c=int(input(print("Üçüncü sayıyı giriniz: ")))
    print(a,b,c)

    bak(a,b,c)


if __name__ == '__main__':
     main()