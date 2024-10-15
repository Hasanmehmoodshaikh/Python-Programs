class Ram():
    def setsize(self):
        self.size="8 GB"
        self.type="DDR 4"
        
    def getsize(self):
        print(f"SIZE    - {self.size}")
        print(f"TYPE    - {self.type}")

class CPU(Ram):
    def setcompany(self):
        self.company="HP"
        self.model="7000 Series"

    def getcompany(self):
        print(f"COMPANY - {self.company}")
        print(f"MODEL   - {self.model}")

class Storage(CPU):
    def setStorage(self):
        self.type="SSD"
        self.size="256 GB"

    def getStorage(self):
        print(f"TYPE    - {self.type}")
        print(f"SIZE    - {self.size}")

class Computer(Storage):

    print("___________")

c1=Computer()
c2=Computer()
c3=Computer()
c4=Computer()

c1.setsize()
c1.setcompany()
c1.setStorage()

c1.getsize()
c1.getcompany()
c1.getStorage()

mylist=[c1,c2,c3,c4]
for i in mylist:
    i.setsize()
    i.setcompany()
    i.setStorage()

for i in mylist:
    i.getsize()
    i.getcompany()
    i.getStorage()
print("____________________")    




