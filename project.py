
def add_student(name,roll_no,marks): 
    myfile = open("student-project/studata.txt","a")
    mydict = {"name":name, "roll_no":roll_no, "marks":marks}
    data = str(mydict)
    myfile.write(f"{data}\n")
    myfile.close()
    print("Student Added Successfully!")
    print("_______________________")

def view_student():
    myfile = open("student-project/studata.txt","r")
    for i in myfile:
        i = eval(i.strip())
        print(f"student name    - {i['name']}")
        print(f"student roll_no - {i['roll_no']}")
        print(f"student marks   - {i['marks']}")
        print("________________")
        
    myfile.close()

def delete_student():
    roll_no = int(input("Enter roll_no to delete:"))
    myfile = open("student-project/studata.txt","r")
    lines = myfile.readlines()
    myfile.close()
    newdata = []
    newdatalines = ""
    print(lines)
    for line in lines:
        line = eval(line.strip())
        # print(line)
        if line['roll_no']!=roll_no:
            newdata.append(str(line)+"\n")
        print(newdata)
    for i in newdata:
        newdatalines+=i
    myfile = open('student-project/studata.txt','w')
    print(newdatalines)
    myfile.write(newdatalines)
    myfile.close()
    
def update_student(roll_no):
    myfile = (open('student-project/studata.txt',"r"))
    lines = myfile.readlines()
    x=[]
    flag=False

    print(lines)
    for i in lines:
        line = i.strip()
        x.append(eval(line))
    print(x)

    for i in x:
        print(i)
        if roll_no==i["roll_no"]:
            new_name=(input("ENTER NEW NAME      - "))
            new_marks=int(input("ENTER NEW MARKS - "))
            i['name'] = new_name
            i['marks'] = new_marks
            flag = True
    print(x)
    
    myfile=(open('student-project/studata.txt',"w"))
    
    data = ""
    for i in x:
        data = data + str(i)+"\n"
    myfile.write(data)
    print("DATA UPDATED SUCCESSFULLY")

while True:
    print("\n Student Management System")
    print("1. ADD STUDENT")
    print("2. VIEW STUDENT")
    print("3. DELETE STUDENT")
    print("4. Update Student")
    print("5. EXIT")
    choice = (input("Enter your choice: "))

    match(choice):
        case '1' :
            name = input("Enter Student name - ")
            roll_no = int(input("Enter student rollno - "))
            marks = int(input("Enter student marks - "))
            add_student(name,roll_no,marks)
        case '2':
            view_student()
        case '3':
            delete_student()
        case '4':
            roll_no = int(input("roll_no - "))
            update_student(roll_no)
            print('\n')
        case '5':
            print("Thanks")
            exit()
        case '':
            print("INVALID INPUT.")
            exit()
            
        