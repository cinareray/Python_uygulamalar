def harfaraligi(sayi):
    notu =int(sayi)

    if notu>=0 and notu<=100:

        if notu<=100 and notu>=90:
            harf = "AA"
        elif notu<90 and notu>=80:
            harf ="BA"
        elif notu<80 and notu>=70:
            harf ="BB"
        elif notu<70:
            harf = "FF"
    else:
        return "Notununz 0-100 arasında değildir...."
    return harf

def main():

        sayi = input("Notunuzu girin:")
        print(harfaraligi(sayi))

if __name__ == '__main__':
    main()