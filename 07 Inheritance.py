class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A): # Single - level inheritance
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

# Writing the name of class A inside the brackets will inherit the features of class A
# Super/Parent class - A
# Sub/Child class - B

class C(B): # Multi - level inheritance
    def feature5(self):
        print("Feature 5 is working")


class D:
    def feature6(self):
        print("Feature 6 is working")

    def feature7(self):
        print("Feature 7 is working")


class E(A,D):   # Multiple inheritance
    def feature8(self):
        print("Feature 8 is working")

    def feature9(self):
        print("Feature 9 is working")


a1 = A()
a1.feature2()
a1.feature1()

b1 = B()    # Single - level inheritance
b1.feature3()
b1.feature4()

c1 = C()    # Multi - class inheritance

e1 = E()    # Multiple inheritance
