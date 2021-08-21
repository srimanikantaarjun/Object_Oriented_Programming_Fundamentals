class Student:
    def __init__(self, name, roll_no):
        self.NAME = name
        self.ROLL_NO = roll_no
        self.LAPTOP = self.Laptop()

    def show(self):
        print(self.NAME, self.ROLL_NO)
        self.LAPTOP.show()

    class Laptop:
        def __init__(self):
            self.BRAND = "HP"
            self.CPU = "i5"
            self.RAM = "8GB"

        def show(self):
            print(self.BRAND, self.CPU, self.RAM)

s1 = Student(name = "Sri", roll_no = 55)
s2 = Student(name = "Mani", roll_no = 35)

# print(s1.NAME, s1.ROLL_NO)

s1.show()
laptop1 = s1.LAPTOP.BRAND
laptop2 = s2.LAPTOP.BRAND
# s1.LAPTOP.show()
