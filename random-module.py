import random as r

print(r.randint(1,50))
print(r.randrange(100,300))

print(r.randint(1000,9999))

students = ['sanjana','suraj','hasanmehmood','mayur','waseem']
print(r.choice(students))

r.shuffle(students)
print(students)