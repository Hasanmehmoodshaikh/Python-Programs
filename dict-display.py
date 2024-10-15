mydict={
    'name':'adnan',         #keys-name #value-adnan
    'city':'solapur',
    'gender':'male',
    'qualification':'BCA'
}

for i in mydict:
    print(f'{i}->{mydict[i]}')
print(mydict.keys())         #dict_keys(['name', 'city', 'gender', 'qualification'])
print(mydict.get('city'))    #solapur
print(mydict.values())      #dict_values(['adnan', 'solapur', 'male', 'BCA'])


for i in mydict.keys(): 
    print(mydict[i])
print("_________________________")

for i in mydict.values():
    print(i)

print(mydict.items())

for i in mydict.items():
    print(i)
print("_________________________")

for i in mydict.items():
    print(i[0],i[1])
print("_________________________")

for i ,j in mydict.items():
    print(i,j)  