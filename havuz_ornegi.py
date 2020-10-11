def main():
    sonuc=0
    musluk = int(input("Kaç musluk var:"))
    for i in range(0,musluk):
        toplam=int(input(str(i+1) + ".musluk kaç saatte dolduruyor."))
        sonuc = sonuc + 1/toplam
    sonuc = 1/sonuc
    print("{} saate doldururlar" .format(sonuc))

if __name__ == '__main__':
    main()