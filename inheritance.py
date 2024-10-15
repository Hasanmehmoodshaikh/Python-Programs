class person:
    name ='Hasanmehmood'
    city = 'solapur'

class student(person):
    rollno =120
    college = "vasundhara"

p = student()
print(p.name)
print(p.city)
print(p.rollno)
print(p.college)
print("______________________________")



class person:
    name = "name" 
    city = "mumbai"

class student(person):
    rollno = 25
    college = 'spm'

p = student()
print(p.name)
print(p.city)
print(p.rollno)
print(p.college)
print("______________________________")
        
class person:
    name = "suraj"
    city = "pune"

class student(person):
    rollno = 21
    college = "vvp"

p = student()
print(f'name    - {p.name}')
print(f'city    - {p.city}')
print(f'rollno  - {p.rollno}')
print(f'college - {p.college}')         