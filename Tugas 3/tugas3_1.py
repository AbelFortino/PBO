import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def tambah(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Operasi ini hanya bisa dilakukan dengan objek Point")
        
    def kurang(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Operasi ini hanya bisa dilakukan dengan objek Point")
        
    def kali(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        else:
            raise TypeError("Operasi ini hanya bisa dilakukan dengan objek Point")

    def bagi(self, other):
        if isinstance(other, Point):
            return Point(self.x / other.x, self.y / other.y)
        else:
            raise TypeError("Operasi ini hanya bisa dilakukan dengan objek Point")
        
    def eksponen(self, other):
        if isinstance(other, Point):
            return Point(self.x ** other.x, self.y ** other.y)
        else:
            raise TypeError("Operasi ini hanya bisa dilakukan dengan objek Point")
        
    def logaritma(self, other):
        if isinstance(other, Point):
            return Point(math.log(self.x, other.x), math.log(self.y, other.y))
        else:
            raise TypeError("Operasi ini hanya bisa dilakukan dengan objek Point")

def print_menu():
    print("\nMenu:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Eksponen")
    print("6. Logaritma")
    print("7. Keluar")

def main():
    print("Masukkan koordinat untuk Point 1:")
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    point1 = Point(x1, y1)

    print("Masukkan koordinat untuk Point 2:")
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    point2 = Point(x2, y2)

    while True:
        print_menu()
        choice = input("Pilih operasi: ")

        try:
            if choice == "1":
                result = point1.tambah(point2)
                print(f"Hasil tambah: ({result.x}, {result.y})")
            elif choice == "2":
                result = point1.kurang(point2)
                print(f"Hasil kurang: ({result.x}, {result.y})")
            elif choice == "3":
                result = point1.kali(point2)
                print(f"Hasil kali: ({result.x}, {result.y})")
            elif choice == "4":
                result = point1.bagi(point2)
                print(f"Hasil bagi: ({result.x}, {result.y})")
            elif choice == "5":
                result = point1.eksponen(point2)
                print(f"Hasil eksponen: ({result.x}, {result.y})")
            elif choice == "6":
                result = point1.logaritma(point2)
                print(f"Hasil logaritma: ({result.x}, {result.y})")
            elif choice == "7":
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()