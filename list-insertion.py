students = ['adnan','jhon','mayur','suraj','addy','bilal','roger']
print(students)
print(len(students))
print(students[5])
print(students[1])
print("___________________________")

# animals = ['dog','fox','cow','rabbit','tiger','lion']
# print(animals)
# print(len(animals))
# print(animals[3])
# print(animals[0])
print("_______________________")

#using append()fun.
students.append("rd")
students.append("sam")
print(students)
print("________________")

#using insert() fun.
students.insert(1,'dd')
print(students)
print("___________________________")

students.insert(360,'bob')
print(students)
print("____________________")

value =input("Enter your name - ")
students.insert(3,value)
print(students)
