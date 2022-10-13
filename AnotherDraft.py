# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def check_mileage(self):
        print(f"Your mileage is {self.mileage}")


modelx = Vehicle(240, 18)
print(modelx.mileage)
