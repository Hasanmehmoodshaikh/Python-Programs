set1 = {'c','c++','python','c#','java'}
set2 = {'php','js','c','python','ruby'}
print(set1)
print(set2)

print(set1.intersection(set2))
print(set2.intersection(set1))
set2.intersection_update(set1)
print(set2)