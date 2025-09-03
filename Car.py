class Car():
    def move(self):
        print("Driving 🚗")

class Plane(Car):
    def __init__(self):
        super().__init__()
    
    def move(self):
        print("Flying ✈️")

        
c1 = Car()
p1 = Plane()

p1.move()
c1.move()