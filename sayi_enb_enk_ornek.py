def main():
    a = int(input("1. sayı :"))
    b=int(input("2.sayi:"))
    c=int(input("3.sayi:"))
    eb=ek=a    #referans noktalarıdır.
    for i in a,b,c:
        if i>eb:
            eb=i
        if i<ek:
            ek=i
    print("En buyuk : ",eb," En kucuk : ",ek)

if __name__ == '__main__':
    main()