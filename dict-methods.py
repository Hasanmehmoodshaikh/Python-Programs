mylist =['x','y','z']
mydict = dict.fromkeys(mylist,100)
print(mydict)

mydict['p']=2000
mydict.setdefault('p',123)
print(mydict)