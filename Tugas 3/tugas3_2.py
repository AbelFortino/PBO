class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type
    
class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child(Father, Mother):
    def __init__(self, father_blood_type, mother_blood_type):
        Father.__init__(self, father_blood_type)
        Mother.__init__(self, mother_blood_type)
        self.blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        if self.blood_type == "A" and self.blood_type == "A":
            return "A"
        elif self.blood_type == "A" and self.blood_type == "B":
            return "AB"
        elif self.blood_type == "A" and self.blood_type == "O":
            return "A"
        elif self.blood_type == "B" and self.blood_type == "B":
            return "B"
        elif self.blood_type == "B" and self.blood_type == "O":
            return "B"
        elif self.blood_type == "O" and self.blood_type == "O":
            return "O"
        else:
            return "AB"
        
def main():
    father_blood_type = input("Masukkan golongan darah ayah: ")
    mother_blood_type = input("Masukkan golongan darah ibu: ")

    child = Child(father_blood_type, mother_blood_type)
    print(f"Golongan darah anak: {child.blood_type}")

if __name__ == "__main__":
    main()