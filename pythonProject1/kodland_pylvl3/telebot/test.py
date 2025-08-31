class Car():
    def __init__(self, atr):
        self.atr = atr

    def __str__(self):
        return f"{self.atr} text"

car = Car(1)
print(car)