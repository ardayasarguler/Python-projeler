isim = []
soyisim = []
sifre = []

liste = f'İsimler: {isim}\nSoyisimler: {soyisim}\nŞifreler: {sifre}'

while True:
    secim = input('1)Kullanıcı Ekle\n2)Kullanıcı Sil\n3)Kullanıcıları Göster\n4)Kullanıcı Girişi\n5)Çıkış Yap\nLütfen Yapmak İstediğiniz İşlemi giriniz:')

    if secim == '1':
        isim_ekle = input('Lütfen İsminizi Giriniz:')
        soyisim_ekle = input('Lütfen Soy isminizi Giriniz:')
        sifre_ekle = input('Lütfen Şifrenizi Giriniz:')
        isim.append(isim_ekle)
        soyisim.append(soyisim_ekle)
        sifre.append(sifre_ekle)
        print(f'{isim_ekle}, Başarıyla Eklenmiştir')
    elif secim == '2':
        isim_sil = input('Lütfen Silmek İstediğiniz ismi Giriniz:')
        soyisim_sil = input('Lütfen Silmek İstediğiniz Soy ismi Giriniz:')
        sifre_sil = input('Lütfen Şifrenizi Giriniz:')
        if isim_sil in isim and soyisim_sil in soyisim and sifre_sil in sifre:
            isim.remove(isim_sil)
            soyisim.remove(soyisim_sil)
            sifre.remove(sifre_sil)
            print(f'{isim_sil}, Başarıyla Silinmiştir')
        else:
            print('Lütfen Tekrar Deneyiniz Böyle Biri Yok')
    elif secim == '3':
        print(liste)
    elif secim == '4':
        isim_giris = input('Lütfen İsminizi Giriniz:')
        soyisim_giris = input('Lütfen Soy isminizi Giriniz:')
        sifre_giris = input('Lütfen Şifrenizi Giriniz:')
        if isim_giris in isim and soyisim_giris in soyisim and sifre_giris in sifre:
            print(f'{isim_giris}, Hoş Geldiniz')
        else:
            print('Lütfen İsim Soyisim Veya Şifrenizi Kontrol Ediniz')
    elif secim == '5':
        print('Çıkılıyor...')
        break
    else:
        print('Lütfen Doğru Seçim Yapınız')
        break