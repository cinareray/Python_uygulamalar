#dongu ile faktoriyel alma

def fak(n):
    sonuc=1
    for i in range(1,n+1):
        sonuc = sonuc * i
    print(sonuc)

def fakto(n):
    if n>0:
        return n*fakto(n-1)
    else:
        return 1
