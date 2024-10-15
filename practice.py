a =(1,5,6,5,4,7,8,9,4,1,0)
b =(1,2,7,9,8,10,6,4,7,3,5)
print(a)
print(a[1:5])
print(a+b)
print(a<b)

a ={1,5,6,5,4,7,8,9,4,1,0}
b ={1,2,7,9,8,10,6,4,7,3,5}

print(a)
print(b)



print(a.union(b))
print(b.update(a))
print(a)

print(a.symmetric_difference(b))
print(b.symmetric_difference_update(a))
print(a)

a =[1,5,6,5,4,7,8,9,4,1,0]
a.append(2)
print(a)

a =[1,5,6,5,4,7,8,9,4,1,0]
a.append('adnan')
print(a)


a ={1,5,6,5,4,7,8,9,4,1,0}
a.update({2,3,10})
print(a)


for i in range(1,6):
    print(i)

for i in range(1,20,2):
    print(i) 

for i in range(1,16):
    for j in range(1,i):
        print(j,end=" ")
        print()


print("______________________________")


# mytuple = ('adnan','mayur','suraj','jhon','oggy','jack')
# (art,enginner,salesman,doctor,singer,rider) =mytuple
# print (salesman)
# print (art)
# print ('jhon')
# print (enginner)
# print (doctor)
# print (singer)
# print (rider)
print("______________________________")


