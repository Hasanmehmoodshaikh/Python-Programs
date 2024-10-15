class Person:
    def setPerson(self):
        self.name = input("Enter Name - ")           #class parent : parent class ka code
        self.city = input("Enter City - ")
    def getPerson(self):
        print(f'Name - {self.name}')
        print(f'city - {self.city}')


class student(Person):
    def setStudent(self):
        self.rollno = int(input('Enter rollno - '))     # class child (parent): child class ka code
        self.college = input('Enter college - ')
    def getStudent(self):
        print(f'Rollno - {self.rollno}')
        print(f'College - {self.college}')

s1 = student()
s2 = student()
s1.setPerson()
s1.setStudent()
print("__________________")

s2.setPerson()
s2.setStudent()
print("__________________")

s1.getPerson()
s1.getStudent()
print("__________________")

s2.getPerson()
s2.getStudent()