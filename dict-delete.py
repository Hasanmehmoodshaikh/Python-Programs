mydict = {'name': 'hasanmehmood',
          'city': 'solapur',
          'gender': 'male',
          'qualification': 'BCA',
          'bloodgroup':'A+',
          'college':'vkmv',
          'passout':'2023',
}

mydict.popitem()
mydict.popitem()
print(mydict)

mydict.pop('bloodgroup')
print(mydict)

del mydict['gender']
print(mydict)

mydict.clear()
print(mydict)

del mydict
print(mydict)