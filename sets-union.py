set1 ={'c','c++','python','java','c#'}
set2 ={'java','js','php','python','c','ruby'}

print(set1)
print(set2)
print(set1.union(set2))
set2.update(set1)
print(set1)
print(set2)

set3 =set1.union(set2)
print(set3)