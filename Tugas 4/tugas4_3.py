class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name:
            raise ValueError("Nama tidak boleh kosong.")
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Usia tidak boleh negatif.")
        self.__age = age

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Tweet!"

def main():
    animals = []

    while True:
        print("\nPilih aksi:")
        print("1. Tambah hewan")
        print("2. Tampilkan suara hewan")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3): ").strip()

        if pilihan == "1":
            try:
                jenis = input("Masukkan jenis hewan (Dog/Cat/Bird): ").strip().capitalize()
                name = input("Masukkan nama hewan: ").strip()
                age = int(input("Masukkan usia hewan: "))

                if jenis == "Dog":
                    animal = Dog(name, age)
                elif jenis == "Cat":
                    animal = Cat(name, age)
                elif jenis == "Bird":
                    animal = Bird(name, age)
                else:
                    raise ValueError("Jenis hewan tidak valid.")

                animals.append(animal)
                print(f"{jenis} bernama {name} berhasil ditambahkan!")
            except ValueError as e:
                print(f"Error: {e}")
        elif pilihan == "2":
            if not animals:
                print("Tidak ada hewan di kebun binatang.")
            else:
                for animal in animals:
                    print(f"{animal.get_name()} ({animal.__class__.__name__}): {animal.make_sound()}")
        elif pilihan == "3":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()