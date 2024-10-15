#required arguments in python
def  area (a,b):
    print("area of rectangl= ", a*b)
area(50,20)
print("____________________")  

#keyword argument in python
def details(name,rank,point):
    print("student name= ",name)
    print("student rank= ",rank)
    print("student point=",point)

details(rank=6,name="addy",point=210.07)
details(point=300.07,rank=5,name="adnan")
print("_______________")

def addtiton(a,b):
 print(a+b)                                 #DEFAULT
addtiton(80,20)
print("________________________________")


def subtraction(a,b):
   n1 = int(input("60-"))                    #DEFAULT
   n2 = int(input("15-"))
print(60-15) 
print("___________________________")

def multiplication():
   n1 = int(input("5-"))
   n2 = int(input("6-"))
   print(f'multiplication of {5} and {6} is {"r"}') #DEFAULT
print(5*6)
print("___________________")

def division(nr,dr):                           # DEFAULT
   return nr // dr
d = division(100,10)
print(d)
print("______________________")


def printMydata(name,city,bloodgroup="NA"):
   print(name)
   print(city)                              #KEYWORD
   print(bloodgroup)

printMydata(bloodgroup="A+",city="solapur",name="ADNAN",) 
printMydata(name="JHON",city="PUNE")  

print("_________________________________")

def printData(*data):
   print(data)
   print(type(data))
   print(len(data))
   print([0])
   print([1])                     #ARBITRARY
   print([2])
   print([3])
   print([4])
print('Addy','Mayur','Suraj','Bilal','Sam','Rd','Jhon')
print("_____________________________")

def printData(**data):
   print(data)
   print(type(data))
   print(len(data))               #KEYWORD arbitrary
   print(data['name'])
   print(data['surname'])
   print(data['city'])
   print(data['rank'])
printData(name='Adnan',surname='Shaikh',city='Solapur',rank=3)   