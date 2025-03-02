dictionary = {}
jumlah_mahasiswa = int(input("Masukkan jumlah siswa:"))

for i in range (1, jumlah_mahasiswa + 1):
    nama = input(f"Masukkan nama siswa ke-{i}: ")
    nilai = int(input(f"Masukkan nilai untuk {nama}: "))
    dictionary[nama] = nilai
   
print("dictionary =", dictionary)