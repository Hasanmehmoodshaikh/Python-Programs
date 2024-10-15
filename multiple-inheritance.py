class Watch:
    def setWatch(self):                                       #grandparent
        self.Watch_features=["Date","Time"]                    # parent1(grandparent)
    def getWatch(self):                                         #parent2(grandparent)
        for i in self.Watch_features:                            #child parent1,parent2
            for i in self.Watch_features:                         
                print(f' - {i}')



class Andriod:
    def setAndroid(self):
        self.androidversion = "Android 15"
        self.smart_features = ['Buletooth','Calling','Health App','Step Count','Music Player']
    def getAndroid(self):
        print(self.androidversion)
        for i in self.smart_features:
            print(f'- {i}')



class SmartWatch(Watch,Andriod):
    def setSmartWatch(self):
        self.brand = 'boAt'
        self.price = 6000
    def getSmartWatch(self):
        print(f'Brand - {self.brand}')
        print(f'Price - {self.price}')


s1 = SmartWatch()
s1.setWatch()
s1.setAndroid()
s1.setSmartWatch()

s1.getWatch()
s1.getAndroid()
s1.getSmartWatch()
