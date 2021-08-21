class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B:
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

# a1 = A()
# b1 = B()

# If we create object of sub class it will first try to find init of Sub class, if it is not found then it will call
# init of Super class
# If we use super(). then it will call init of Super class then call init of Sub class

class C(A, B):
    def __init__(self):
        super().__init__()
        print("in C init")

c1 = C()

# METHOD RESOLUTION ORDER
# To represent Super class we use super(). method
