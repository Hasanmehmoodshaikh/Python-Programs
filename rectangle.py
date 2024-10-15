class rectangal:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length*self.width

    def calculate_perimetre(self):
        return 2*(self.length+self.width)
print(f'area:{rectangal.calculate_area()}')
print(f'perimeter:{rectangal.calculate_primeter()}')


