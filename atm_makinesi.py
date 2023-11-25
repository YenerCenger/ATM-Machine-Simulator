print("""**************************
Atm Makinesine Hoşgeldiniz

İşlemler;

1. Bakiye Sorgulama

2. Para Çekme

3. Para Yatırma

Programdan Çıkmak için 'q' ya basın

**************************
""")

bakiye = 1000
atm_şifre = "123"
giriş_hakkı = 3

while True:
    if atm_şifre == input("Atm sifresini Giriniz:"):

        while True:
            işlem = input("İşlemi Seçiniz:")

            if işlem == "q":
                print("Yine Bekleriz.")
                break

            elif (işlem == "1"):
                print("Bakiyeniziz {} tldir.".format(bakiye))

            elif (işlem == "2"):
                miktar = int(input("Miktarı Giriniz:"))
                bakiye += miktar

            elif (işlem == "3"):
                miktar = int(input("Miktarı Giriniz:"))
                if bakiye - miktar < 0:
                    print("Yetersiz Bakiye.")
                    continue
                bakiye -= miktar

            else:
                print("Geçersiz İşlem")

    else:
        print("Geçersiz Şifre")
        giriş_hakkı -= 1
        if giriş_hakkı == 0:
            print("Hesap Kitleniyor...")
            break












