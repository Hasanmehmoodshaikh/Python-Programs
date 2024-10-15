employees = {}
def insert_employee():
    id = input("Enter ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    department = input("Enter department: ")
    salary = input("Enter salary: ")
    employees[id] ={"name":name,"age":age,"department":department,"salary":salary}
    print("Employee added!")

def delete_employee():
    id =input("Enter ID to delete:")
    if id in employees:
        del employees[id]
        print("Employee deleted!")
    else:
        print("Employee not found!")

def display_employees():
    for id,employee in employees.items():
        print(f"ID:{id}")
        print(f"Name:{employee['name']}")
        print(f"Age:{employee['age']}")
        print(f"Department:{employee['department']}") 
        print(f"Salary:{employee['salary']}") 
        print("_______________________________")          

while True:
    print("1.Insert Employee")
    print("2.Delete Empolyee")
    print("3.Display Employees")
    print("4.Exit")
    choice = input("Enter your choice:")

    if choice =="1":
        insert_employee()
    elif choice =="2":
        delete_employee()
    elif choice =="3":
        display_employees()
    elif choice =="4":
        break
    else: 
        print("Invalid choice. Please try again.")