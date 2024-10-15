mylist= ['10','20','30','40','50','60','70','80','90','100']
for i in range(3):
    mylist.append(input("Enter Value - "))
print(mylist)
print("__________________")

for i in mylist:
    print(i)
print("__________________")

for i in range(len(mylist)):
    print(f'{i}->{mylist[i]}')
print("__________________")   

for i in range(0,len(mylist),2):
    print(mylist[i])
print("__________________")   

print(mylist[5:10])
print(mylist[0:7:3])
mylist.pop()
print(mylist)
mylist.insert(4,55)
print(mylist)
print(mylist[-3:])