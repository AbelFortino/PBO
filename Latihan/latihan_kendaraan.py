class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum
    
    def info_kendaraan(self):
        print(f"Jenis Kendaraan = {self.jenis}")
        print(f"Kecepatan Maksimum = {self.kecepatan_maksimum}")
    
    def bergerak(self):
        print("Mobil sedang bergerak")

class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu

    def info_mobil(self):
        print(f"Merk Mobil = {self.merk}")
        print(f"Jumlah Pintu = {self.jumlah_pintu}")

    def bunyikan_kalkson(self):
        print("Beep BEEEEEEEP")

class MobilSport(Mobil):    
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda
        self.__harga = harga

    def get_tenaga_kuda(self):
        return self.__tenaga_kuda

    def set_tenaga_kuda(self, value):
        self.__tenaga_kuda += value

    def get_harga(self):
        return self.__harga

    def set_harga(self, value):
        self.__harga += value

    def info_mobil_sport(self):
        return self.info_mobil

    def mode_balap(self):
        print("Mode Balap ON")

mobilsport = MobilSport("Darat", 294, "BMW", 4, 410, 2)
mobilsport.info_mobil_sport()
mobilsport.bergerak()
mobilsport.bunyikan_kalkson()
mobilsport.mode_balap()
mobilsport.set_tenaga_kuda(100)
mobilsport.set_harga(1)
print(f"Tenaga Kuda Mobil ini adalah = {mobilsport.get_tenaga_kuda()} HP")
print(f"Harga Mobil ini adalah = {mobilsport.get_harga()}M")