class employee:
    def __init__(self,empid,empname,empsalary):
        self.empid = empid
        self.empname = empname
        self.empsalary = empsalary

    def getemployee(self):
        print(f'employee id - {self.empid}')
        print(f'employee name - {self.empname}')
        print(f'employee salary - {self.empsalary}')

s1 = employee(101,'adnan',25000) 
s2 = employee(123,'mayur',30000)  


s1.getemployee()
s2.getemployee()
 
print("____________________________________")




    