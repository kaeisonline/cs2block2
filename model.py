
B = "blue"
R = "red"
G = "gray"
O = "orange"
Y = "yellow"
print(f"{B}, {R}, {G}, {O}, {Y}")
 
print('this is model')
print("hello")
print("rex")
print("spled")
print("nicolle")
print("aneza")
print("carla")
print("marv")
print("cy")
print("bry")
print("patrik")

class student:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def details(self):
        print("{} {} - {}".format(self.first, self.last, self.age))

std = student("Lexus", "Taladro", 22)
std.details()
