class Car:
    TIRES = 4   # CLASS/STATIC VARIABLE
    def __init__(self):
        self.MIL = 10       # INSTANCE VARIABLES
        self.COM = "BMW"    # INSTANCE VARIABLES


c1 = Car()
c2 = Car()

c1.MIL = 8

Car.TIRES = 6
print(c1.COM, c1.MIL, c1.TIRES)
print(c2.COM, c2.MIL, c2.TIRES)
