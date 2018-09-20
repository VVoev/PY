class Circle():

    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r

    def get_radius(self):
        return self.radius


krug = Circle(2)
print(krug.calculateArea())
krug.set_radius(100)
print(krug.calculateArea())
print(krug.get_radius())
