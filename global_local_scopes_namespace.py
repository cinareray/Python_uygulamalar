def struck():
    def local_degisken():
        era = "local degisken"
        print(era)
    def nonlocale_degisken():
        nonlocal era
        era = "nonlocak degisken"
    def global_degisken():
        global era
        era ="Global degisken"
    era = "era baslangıç"
    local_degisken()
    print("locak_degislenden sonra :", era)
    nonlocale_degisken()
    print("nonlocal_degiskenden sonra : ", era)
    global_degisken()
    print("global_degiskenden sonra: ", era)


def main():
    struck()
    print(era)



if __name__ == '__main__':
    main()