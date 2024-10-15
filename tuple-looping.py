mytuple =('mayur','adnan','suraj','jhon','waseem')
print(mytuple[0])
print(mytuple[2])
print(mytuple[4])
print(mytuple[1])
print(mytuple[3])
print("__________________________________")

for i in mytuple:
    print(i)
print("__________________________________")

for i in range(len(mytuple)):
    print(f'{i}->{mytuple[i]}')