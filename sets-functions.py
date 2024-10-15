mysets ={'ruby','js','c++','python','php','c#','c','html'}
set1 = {'c','c++','python','c#','java'}
set2 = {'php','js','c','python','ruby'}
set3 = {'kolin','r','sql','c'}
print(set1.issubset(mysets))
print(set2.issubset(mysets))

print(mysets.issubset(set1))
print(mysets.issubset(set2))
print(set1.isdisjoint(set3))