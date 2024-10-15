mylist = ['jhon','mayur','adnan','suraj','rohit','rafu','bob']
print(mylist)
mylist[2]='adnan shiakh'
print(mylist)
print("_____________________________")

index =int(input("Enetr Index - "))
if index<len(mylist):
    value =input("Enter Value - ")
    mylist[index] =value
    print("LIST DATA CHANGED SUCCESSFULLY ")
else:
    print("INVALED INDEX, NO CHANGE IN THE LIST ")
print(mylist)    