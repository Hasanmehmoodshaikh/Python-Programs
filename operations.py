class circle:
    pi = 3.14

    def setRadius(self,radius):
        self.radius = radius

    def getRadius(self):
        print(f'Radius of circle is - {self.radius}')

    def area(self):
        print(f'Area of circle is - {self.pi * self.radius ** 2}')

    def circumference(self):
        print(f'circumference of circle is - {2 * self.pi * self.radius}')

c1 = circle()
c2 = circle()
c3 = circle()

c1.setRadius(2)
c2.setRadius(5)
c3.setRadius(10)

print('Information About Circle 1')
c1.getRadius()
c1.area()
c1.circumference()
print('_________________________')
print('Information About Circle 2')
c2.getRadius()
c2.area()
c2.circumference()
print('_________________________')
print('Information About Circle 3')
c3.getRadius()
c3.area()
c3.circumference()
