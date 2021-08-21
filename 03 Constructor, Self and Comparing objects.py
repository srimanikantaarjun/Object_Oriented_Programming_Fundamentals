class Computer:
    def __init__(self):
        self.NAME = "Sri"
        self.AGE = 24

    def update(self):
        self.AGE = 26

    def compare(self, other):
        if self.AGE == other.AGE:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()

# print(c1.NAME)
# c1.NAME = "Mani"
# print(c1.NAME)
# print(c1.AGE)
c1.AGE = 25
# print(c1.AGE)

if c1.compare(c2):
    print("They are same")
else:
    print("They are different.")

c1.update()

print("\n")

# print(id(c1))
# print(id(c2))
print(c2.NAME)
