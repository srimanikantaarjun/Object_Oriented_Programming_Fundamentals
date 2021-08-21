
class Computer:
    def __init__(self, CPU, RAM):
        self.CPU = CPU
        self.RAM = RAM

    def config(self):
        print("Configuration is ", self.CPU + " and", self.RAM)

com1 = Computer("i5", "16GB")
com2 = Computer("Ryzen 3", "8GB")

com1.config()
com2.config()
