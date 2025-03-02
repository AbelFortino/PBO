nama = str(input("Nama : "))
asal = str(input("Asal : "))

with open('readme.txt', 'w') as f:
    f.write(nama)
    f.write(asal)