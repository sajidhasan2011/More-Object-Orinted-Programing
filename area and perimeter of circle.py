class Circle():
    def __init__(self,r) :
        self.radius = r

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

radius = float(input("Enter Radius :"))
NewCircle = Circle(radius)

print(f"Area of circle: {NewCircle.area()}")
print(f"Perimeter of circle: {NewCircle.perimeter()}" )