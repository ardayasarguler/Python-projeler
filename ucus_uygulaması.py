
class Ucus:
    def __init__(self, ucus_no, kalkis, varis, saat, kapasite):
        self.ucus_no = ucus_no
        self.kalkis = kalkis
        self.varis = varis
        self.saat = saat
        self.kapasite = int(kapasite)
        self.yolcular = []

    def bos_koltuk_sayisi(self):
        return self.kapasite - len(self.yolcular)

    def ucus_bilgisi_getir(self):
        return f"[{self.ucus_no}] {self.kalkis} -> {self.varis} | Saat: {self.saat} | Boş Koltuk: {self.bos_koltuk_sayisi()}"


class UcusYardimcisi:
    def __init__(self):
        self.ucus_listesi = [
            Ucus("TK1910", "Ankara", "Bursa", "19.10", 17),
            Ucus("TK1964", "Bursa", "Ankara", "17.00", 9),
            Ucus("TK2026", "Erzurum", "Ankara", "15.00", 3)
        ]

    def menu_goster(self):
        print("\n--- Türk Havayolları Uçuş Planlayıcısı ---")
        print("HOŞGELDİNİZ")
        print("1) Tüm uçuşları listele")
        print("2) Nereye gitmek istersiniz (Rota Sorgula)")
        print("3) Bilet al")
        print("4) Çıkış")

    def ucuslari_listele(self):
        print("\nMevcut Uçuşlar:")
        for ucus in self.ucus_listesi:
            print(ucus.ucus_bilgisi_getir())

    def rota_sorgula(self):
        hedef = input("Lütfen gitmek istediğiniz şehri yazınız: ").capitalize()
        bulundu = False
        for ucus in self.ucus_listesi:
            if ucus.varis == hedef:
                print(f"Uygun uçuş bulundu: {ucus.ucus_bilgisi_getir()}")
                bulundu = True

        if not bulundu:
            print(f"Üzgünüz, {hedef} şehrine şu anlık uçuş bulunmuyor :(")

    def bilet_al(self):
        self.ucuslari_listele()
        secim_no = input("\nBilet almak istediğiniz uçuş numarasını girin (Örn: TK1910): ").upper()

        hedef_ucus = None
        for ucus in self.ucus_listesi:
            if ucus.ucus_no == secim_no:
                hedef_ucus = ucus
                break

        if hedef_ucus:
            if hedef_ucus.bos_koltuk_sayisi() > 0:
                isim = input("Yolcunun adını ve soyadını giriniz: ")
                hedef_ucus.yolcular.append(isim)
                print(f"İşlem Başarılı! Sayın {isim}, biletiniz kesildi.")
            else:
                print("Hata: Bu uçuşta hiç boş koltuk kalmamış!")
        else:
            print("Hata: Geçersiz uçuş numarası girdiniz.")


planlayici = UcusYardimcisi()

while True:
    planlayici.menu_goster()
    secim = input("\nYapmak istediğiniz işlemi seçiniz (1-4): ")

    if secim == "1":
        planlayici.ucuslari_listele()
    elif secim == "2":
        planlayici.rota_sorgula()
    elif secim == "3":
        planlayici.bilet_al()
    elif secim == "4":
        print("Türk Havayolları iyi uçuşlar diler, hoşça kalın!")
        break
    else:
        print("Geçersiz seçim! Lütfen 1 ile 4 arasında bir sayı giriniz.")