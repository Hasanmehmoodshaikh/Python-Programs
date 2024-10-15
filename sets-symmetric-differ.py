set1 = {'c','c++','python','c#','java'}
set2 = {'php','js','c','python','ruby'}

set3 = set1.symmetric_difference(set2)
print(set3)

set2.symmetric_difference_update(set1)
print(set1)