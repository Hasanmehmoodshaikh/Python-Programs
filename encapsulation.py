class pen:
    def __init__(self,company,model,price):
        self.__company = company
        self.__model = model
        self.__price = price

    def setCompany(self,c):
        self.__company = c
    def getCompany(self):
        return self.__company
    
    def setModel(self,m):
        self.__model = m

    def getModel(self):
        return self.__model
    
    def setPrice(self,p):
        self.__price = p

    def getPrice(self):
        return self.__price 

p1 = pen('cello','Butterflow',15)
p2 = pen('Raynolds','liquiflow',25)
p3 = pen('Trimax','F',45)
p4 = pen('Parker','p',40)

print('Data of pen 1')
print(f'company - {p1.getCompany()}')
print(f'model - {p1.getModel()}')
print(f'price - Rs. {p1.getPrice()}')
print("_____________________")

print('Data of pen 2')
print(f'company - {p2.getCompany()}')
print(f'model - {p2.getModel()}')
print(f'price - Rs. {p2.getPrice()}')
print("_____________________")

print('Data of pen 3')
print(f'company - {p3.getCompany()}')
print(f'model - {p3.getModel()}')
print(f'price - Rs. {p3.getPrice()}')
print("_____________________")

print('Data of pen 4')
print(f'company - {p4.getCompany()}')
print(f'model - {p4.getModel()}')
print(f'price - Rs. {p4.getPrice()}')
print("_____________________")

p3.setPrice(60)
print("Data of pen 3 after change")
print(f'Company - {p3.getCompany()}')
print(f'model - {p3.getModel()}')
print(f'price - Rs. {p3.getPrice()}')
