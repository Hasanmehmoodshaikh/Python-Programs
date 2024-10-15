x = list()
print(type(x))



class student:
    def setStudent(self):
        self.rollno = int(input("Enter Roll No - "))
        self.name = input("Enter Name - ")
        self.marks = float (input("Enter Marks - "))
    def getStudent(self):
        print(f'Roll No - {self.rollno}')
        print(f'Name    - {self.name}')
        print(f'Marks   - {self.marks}') 
s1 = student()
print(type(s1))

# print(s1.rollno)
# print(s1.name)
# print(s1.marks)
# print("________________________")

# s2 = student()
# print(s2.rollno)
# print(s2.name)
# print(s2.marks)
# print("_______________________")

s1.setStudent() #call
s1.getStudent()