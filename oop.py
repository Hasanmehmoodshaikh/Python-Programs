# class employe:
#     employe_id = 101                                                     # int
#     employe_name = 'jack'                                                # 'str'
#     employe_salary =25000                                                #  int

#     def Setemploye(self):
#         self.employe_id = int(input("Enter Yuor Id - "))
#         self.employe_name = input ("Enter Your Name - ")
#         self.employe_salary =int (input("Enter Your Salary - "))

#     def GetEmploye(self):                                                            # Setemploye : Snake case
#         print(f'emlpoye_Id = {self.employe_id}')                                    # GetEmploye : camel case
#         print(f'employe_name = {self.employe_name}')
#         print(f'emlopye_salary = {self.employe_salary}')
# s3 = employe()
# s3.Setemploye()
# s3.GetEmploye()
print("______________________________")

# class student:
#     student_name ='hasan'               # 'str'
#     student_rollno = 1                  # int 
#     student_marks = 45.20               # folt

#     def Setstudent(addy):
#         addy.student_name = input("Enter Your Name - ")
#         addy.student_rollno = int(input("Enter Your Rollno - "))
#         addy.student_marks = input("Enter Your Marks - ")

#     def GetStudent(addy):
#         print(f'student_name ={addy.student_name}')
#         print(f'student_rollno ={addy.student_rollno}')
#         print(f'student_marks ={addy.student_marks}')

# result = student()
# result.Setstudent()
# result.GetStudent() 
print("_______________________________________")


class student:
    def SetStudent(self):
        self.student_name = input("Enter Your Name - ")
        self.student_passout = int(input("Enter Your passout - "))
        self.student_id = int(input("Enter Yuor Id - "))
    
    def GetStudent(self):
        print(f'student_name = {self.student_name}')
        print(f'student_passout ={self.student_passout}')
        print(f'student_id ={self.student_id}')


result = student()
result.SetStudent()
result.GetStudent()        