para = "12500"
isim = ['Arda']
soyisim = ['Arda']
sifre = ['Arda']
giris = input("Terminal Bankasına Hoşgeldiniz\n1)Giriş Yap\nLütfen Yapmak İstediğiniz İşlemi Seçiniz:")
if giris == "1":
    giris_isim=input("lütfen İsminizi Giriniz:")
    giris_sifre=input("Lütfen Şifrenizi Giriniz:")
elif giris == "2":
    ekle_isim = input("Lütfen İsminizi Giriniz:")
    ekle_soyisim = input("Lütfen Soyisminizi Giriniz:")
    ekle_tc = input("Lütfen TC Giriniz:")
    ekle_sifre = input("Lütfen Sifre Giriniz:")
    isim.append(ekle_isim)
    sifre.append(ekle_sifre)
    tc.append(ekle_tc)
    soyisim.append(ekle_soyisim)
    print(f"{ekle_isim} Hoşgeldiniz Kayıt Başarılı")
else:
    print("Yanlış Seçim")
while True:
    if giris_isim in isim and giris_sifre in sifre:
        ana_menu = input(f"Merhaba {giris_isim} Hoşgeldin\n1)Para Çek\n2)Para Yükle\n4)Çıkış Yap\nLütfen Yapmak İstediğiniz İşlemi Seçiniz:")
        if ana_menu == "1":
            sil_para = int(input("Lütfen Çekeceğiniz Parayı Yazınız:"))
            if sil_para < int(para):
                son_para = int(para) - int(sil_para)
                print(f"İşlem Başarılı Bakiyeniz:{son_para}")
        elif ana_menu == "2":
            ekle_para = int(input("Lütfen Yatıracağınız Parayı Giriniz:"))
            ekle_son_para = int(para) + int(ekle_para)
            print(f"İşlem Başarılı Bakiyeniz:{ekle_son_para}")
        elif ana_menu == "3":
            print(f"Toplam Bakiyeniz{para}")
        elif ana_menu == "4":
            print("Çıkılıyor")
            break
        else:
            print("Yanlış Veya Geçersiz Bir Seçim Yaptınız Çıkılıyor")
            break
