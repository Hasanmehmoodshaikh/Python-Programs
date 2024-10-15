def addEmployee(EMPLOYEE_ID,EMPLOYEE_NAME,EMPLOYEE_CITY,EMPLOYEE_SALARY):
  MYDICT=open("EMPLOYEE_MANAGEMENT_SYSTEM" ,"a")
  data={"ID":EMPLOYEE_ID,"NAME":EMPLOYEE_NAME,"CITY":EMPLOYEE_CITY,"SALARY":EMPLOYEE_SALARY}
  x=str(data)
  x=x.upper()
  MYDICT.write(f"{x}\n")
#_______________________________________________________#
def viewAll():
   mydict=open("EMPLOYEE_MANAGEMENT_SYSTEM","r")
   mylist=list(mydict)
   for i in range(0,len(mylist)):
     print("                                                                                                ")
     print("________________________________")
     print(mylist[i])
     print("                                                                                                ")
#_______________________________________________________#
def viewSingle(EMPLOYEE_NAME):
  mydict=(open("EMPLOYEE_MANAGEMENT_SYSTEM","r"))
  print(EMPLOYEE_NAME)
  flag=False
  for i in mydict:

     i=i.strip()
     if EMPLOYEE_NAME in i:
      flag=True
      print("                                                                                                ")
      print("________________________________")
      print(i)
      print("                                                                                                ")
  if flag==False:
      print("DATA IS NOT EXIST")
      print("                 ")
#_______________________________________________________#    
def deleteEmployee(EMPLOYEE_NAME,EMPLOYEE_CITY):
  mydict=(open("EMPLOYEE_MANAGEMENT_SYSTEM","r"))
  flag=False
  data=mydict.readlines()
  X=[]
  for i in data:
    record=eval(i.strip())

    if not(record['NAME']==EMPLOYEE_NAME and record['CITY']==EMPLOYEE_CITY):
         X.append(i)

    else:
      flag=True


  if flag==True:
      print("--------------DATA IS DELETED--------------")
      print("                                           ")
  else:
      print("???? DATA IS NOT EXIST")
      print("                                            ")   
  dict=(open("EMPLOYEE_MANAGEMENT_SYSTEM","w"))   
  dict.writelines(X)
#_______________________________________________________
def changeEmployeeDetails(EMPLOYEE_NAME,EMPLOYEE_CITY):
  mydict=(open("EMPLOYEE_MANAGEMENT_SYSTEM","r"))

  lines=mydict.readlines()
  X=[]
  flag=False

  for i in range(len(lines)):
   line=lines[i].strip()
   if line:
      data=eval(line)

      if data["NAME"]==EMPLOYEE_NAME and data["CITY"]==EMPLOYEE_CITY:

         new_id=int(input("ENTER NEW ID - "))
         new_name=(input("ENTER NEW NAME - "))
         new_city=(input("ENTER NEW CITY - "))
         new_salary=int(input("ENTER NEW  SALARY - "))
         new_name=new_name.upper()
         new_city=new_city.upper()
         flag=True
         data["ID"]=new_id
         data["NAME"]= new_name
         data["CITY"]= new_city
         data["SALARY"]=  new_salary
         lines[i]=str(data) +'\n'

  if flag==True:
     print("                                             ")
     print("---------------DATA IS CHANGED---------------")
  else:
     print("???? DATA IS NOT EXIST")
     print("                                            ")   

  MYDICT=open("EMPLOYEE_MANAGEMENT_SYSTEM","w")
  MYDICT.writelines(lines)




#_______________________________________________________#
#_______________________________________________________#  
X='Y'
while X=='Y':
  print("               ")
  print("!!__WELCOME TO EMPLOYEE MANAGEMENT SYSTEM__!!")
  print("               ")
  print("1.ADD NEW EMPLOYEE_DETAILS")
  print("2.VIEW ALL EMPLOYEE_DETAILS")
  print("3.SEARCH EMPLOYEE_DETAILS")
  print("4.DELETE EMPLOYEE_DETAILS")
  print("5.CHANGE EMPLOYEE_DETAILS")
  print("6.EXIT")
  try:
    CHOICE=int(input("ENTER YOUR CHOICE - "))
  except:
     print("???PLEASE SELECT IN NUMBERS")


  match(CHOICE):
    case 1:
      try:
         EMPLOYEE_ID=int(input("ENTER EMPLOYEE ID -"))
         EMPLOYEE_NAME= input("ENTER EMPLOYEE NAME - ")
         EMPLOYEE_CITY=input("ENTER EMPLOYEE CITY - ")
         EMPLOYEE_SALARY=int(input("ENTER EMPLOYEE SALARY -"))
         addEmployee(EMPLOYEE_ID,EMPLOYEE_NAME,EMPLOYEE_CITY,EMPLOYEE_SALARY)
         print("                                            ")
         print("-----------EMPLOYEE_DETAILS ADDED-----------")
         print("                                            ")
      except ValueError:
         print("???? PLEASE ENTER NUMBERS IN EMPLOYEE_ID AND SALARY")

    case 2:
       viewAll()

    case 3:
      EMPLOYEE_NAME=input("ENTER EMPLOYEE_NAME - ")
      EMPLOYEE_NAME=EMPLOYEE_NAME.upper()
      viewSingle(EMPLOYEE_NAME)

    case 4:
      EMPLOYEE_NAME=input("ENTER EMPLOYEE NAME - ")
      EMPLOYEE_CITY=input("ENTER EMPLOYEE CITY  - ")
      EMPLOYEE_NAME=EMPLOYEE_NAME.upper()
      EMPLOYEE_CITY=EMPLOYEE_CITY.upper()
      deleteEmployee(EMPLOYEE_NAME,EMPLOYEE_CITY)

    case 5:
      EMPLOYEE_NAME=input("ENTER EMPLOYEE NAME - ")
      EMPLOYEE_CITY=input("ENTER EMPLOYEE CITY  - ")

      EMPLOYEE_NAME=EMPLOYEE_NAME.upper()
      EMPLOYEE_CITY=EMPLOYEE_CITY.upper()
      changeEmployeeDetails(EMPLOYEE_NAME,EMPLOYEE_CITY)
      print('\n')


    case 6:
        print("------------THANK YOU------------")
        exit()

    case _:
        print("??? PLEASE SELECT CORRECT CHOICE")

  X=input("DO YOU CONTINUE (Y|yes and N|no) - ")
  X=X.upper()
  if X!='N' and X!='Y':
     X=input("DO YOU CONTINUE (Y|yes and N|no) - ")


print("------------THANK YOU------------")