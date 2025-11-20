class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.year} {self.brand} {self.model}"

    def is_classic(self):
        current_year = 2024
        return (current_year - self.year) > 20
      
car1 = Car("Toyota", "Corolla", 2000)
print(car1.get_description())
print("Is classic car:", car1.is_classic())