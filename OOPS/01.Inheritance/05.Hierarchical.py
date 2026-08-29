# ============================================================
# 4. HIERARCHICAL INHERITANCE
# One Parent Class → Multiple Child Classes
# ============================================================

class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "vehicle is starting")


class Car(Vehicle):

    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def drive(self):
        print(self.brand, "car is driving")


class Bike(Vehicle):

    def __init__(self, brand, gears):
        super().__init__(brand)
        self.gears = gears

    def ride(self):
        print(self.brand, "bike is riding")


car = Car("Toyota", 4)

print("\nCar Brand:", car.brand)
print("Number of Doors:", car.doors)

car.start()       # Inherited from Vehicle
car.drive()


bike = Bike("Honda", 5)

print("\nBike Brand:", bike.brand)
print("Number of Gears:", bike.gears)

bike.start()      # Inherited from Vehicle
bike.ride()

