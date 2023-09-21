class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

my_car = Car("Toyota", "Camry", 2022)

print("Make:", my_car.make)
print("Model:", my_car.model)
print("Year:", my_car.year)

print("Car Description:", my_car.description())
