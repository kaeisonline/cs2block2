class student:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def details(self):
        print("{} {} - {}".format(self.first, self.last, self.age))

std = student("Lexus", "Taladro", 22)
std.details()