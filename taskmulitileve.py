class Phone: 
    def setPhone(self):
        self.Brand = 'Nokia'
        self.Model = "a15"
        self.colour = "Black"
    def getPhone(self):
        print(f"Brand          - {self.Brand}")
        print(f"Model          -  {self.Model}")
        print(f"colour         - {self.colour}")

class Mobilephone(Phone):
    def setMobilephone(self):
        self.features  = ["Touchscreen","wifi","GPS","calling"]
    def getMobileFeatures(self):
        print(f"Features       - {self.features}")

class Smartphone(Mobilephone):
    def setSmartfeatures(self):
        self.smartFeatures = ["Fingerprint sensor","Games","Videocalling","5G Network","Ai"]
        self.price ="15000 Rs" 
    def getSmartfeatures(self):
         print(f'smartFeatures  - {self.smartFeatures}')
         print(f'Price          - {self.price}')


p1 = Smartphone()
p1.setPhone()
p1.setMobilephone()       #bht mehnga hai phn itne kam features me 😂
p1.setSmartfeatures()
p1.getPhone()
p1.getMobileFeatures()
p1.getSmartfeatures()

