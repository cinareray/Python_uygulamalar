#girilen sayıya kadar asal sayıları ekrana yazdıran program
sonuc = []
x = int(input("Sayı girininiz :"))
for i in range(1,x):
    for ii in range(2,i):
        if(i%ii==0):
            break
    else:                #else yapısı for dongusunun altında dıkkat et !!!!
        sonuc.append(i)
print(sonuc)



