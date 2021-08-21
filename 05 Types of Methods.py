# import sys
# sys.stdout = open("test.txt", "w")

class Student:
    SCHOOL = "High School"  # CLASS VARIABLE
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):      # INSTANCE METHOD
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):       # ACCESSOR METHOD
        return self.m1

    def set_m1(self, value):    # MUTATOR METHOD
        self.m1 = value

    @classmethod        # --> We need to use decorator to define a class method
    def get_SCHOOL(cls):      # CLASS METHOD
        return cls.SCHOOL

    @staticmethod
    def info():
        print("This is Student class . . . in ABC module")

# To work with instance variables we use instance methods --> average, get_m1, set_m1 . . .
# To work with class variables we use class methods --> info . . .
# To do something extra using our class use Static methods nothing to do with our instance/class/static variable . . .
s1 = Student(m1 = 34, m2 = 47, m3 = 32)
s2 = Student(m1 = 89, m2 = 32, m3 = 12)

print(s1.average())
print(s2.average())
print(Student.get_SCHOOL())
Student.info()
# sys.stdout.close()
