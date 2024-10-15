set1 = {'c','c++','python','c#','java'}
set2 = {'php','js','c','python','ruby'}
print(set1.difference(set2))
#print(set1-set2)
set2.difference_update(set1)
print(set1)
print(set2)
print("______________________________")


name1 = {'hasan','adnan','Rd','bilal'}
name2 = {'adnan','arfat','zameer','umar'}
print (name1.difference(name2))
print (name2.difference(name1))


name3 = name1.union(name2)
print(name3)
print("______________________________")


name2.difference_update(name1)
print(name2)
name3.difference_update(name2)
print(name3)
name1.difference_update(name3)
print(name1)