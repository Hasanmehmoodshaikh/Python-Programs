class Box:
    def setBox(self):
        self.width = "300 cm"               #grand parent
        self.height = "200 cm"               #parent(G-parent)
    def getBox(self):                         #child (parent)
        print(f'Width - {self.width}')
        print(f'Height - {self.height}')

class ColoredBox(Box):
    def setColor(self):
        self.color = 'white'
    def getColor(self):
        print(f'color - {self.color}')

class ShippedBox(ColoredBox):
    def setShipping(self):
        self.weight = "500 cm"
        self.cost = "INR. 2000"
    def getShipping(self):
        print(f'weight - {self.weight}')
        print(f'cost - {self.cost}')

s1 = ShippedBox()
s1.setBox()
s1.setColor()
s1.setShipping()
s1.getBox()
s1.getColor()
s1.getShipping()        
