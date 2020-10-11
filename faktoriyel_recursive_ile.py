def fak(sayi):
    if 0<sayi:
       return sayi*fak(sayi-1)  #özyineli fonksiyon recursive
    else:
        return 1

def main():
    sayi =int(input("Faktoriyeli alınacak sayi:"))
    print(fak(sayi))


if __name__ == '__main__':
        main()
