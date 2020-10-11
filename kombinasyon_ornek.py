# c(n,r) = n! / (r!(n-r)!)  kombinasyon işlemi
def n_hesaplama(n):
    sonuc=1
    if n>0:
        return n * n_hesaplama(n-1)
    else:
        return 1

def main():
    n=int(input("1.sayıyı giriniz:"))
    r=int(input("2.sayıyı giriniz:"))
    sonuc = n_hesaplama(n)
    sonuc2 = n_hesaplama(r)
    sonuc3 = n_hesaplama(n-r)
    son = sonuc / (sonuc2 * sonuc3)
    print( "({}/{}) \nkombinasyonun Sonucu : {}" .format(n, r, son))

if __name__ == '__main__':
    main()