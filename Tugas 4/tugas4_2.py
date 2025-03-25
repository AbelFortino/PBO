def tambah_tugas(daftar_tugas):
    tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
    if not tugas:
        raise ValueError("Tugas tidak boleh kosong.")
    daftar_tugas.append(tugas)
    print("Tugas berhasil ditambahkan!")

def hapus_tugas(daftar_tugas):
    try:
        nomor_tugas = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if nomor_tugas < 1 or nomor_tugas > len(daftar_tugas):
            raise IndexError("Tugas dengan nomor tersebut tidak ditemukan.")
        tugas = daftar_tugas.pop(nomor_tugas - 1)
        print(f"Tugas '{tugas}' berhasil dihapus!")
    except ValueError:
        print("Input tidak valid. Harap masukkan nomor tugas yang valid.")
    except IndexError as e:
        print(f"Error: {e}")

def tampilkan_daftar_tugas(daftar_tugas):
    if not daftar_tugas:
        print("Daftar tugas kosong.")
    else:
        print("Daftar Tugas:")
        for index, tugas in enumerate(daftar_tugas, start=1):
            print(f"{index}. {tugas}")

def main():
    daftar_tugas = []
    while True:
        print("\nPilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()

        if pilihan == "1":
            try:
                tambah_tugas(daftar_tugas)
            except ValueError as e:
                print(f"Error: {e}")
        elif pilihan == "2":
            hapus_tugas(daftar_tugas)
        elif pilihan == "3":
            tampilkan_daftar_tugas(daftar_tugas)
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()