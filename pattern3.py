for i in range(1,7):            #1
    for j in range(1,7-i):
        print('*',end=' ')
    print()
print("____________________")



for i in range(1,7):            #2
    for j in range (1,i+1):
        print('*',end=' ')
    print()
print("_____________")


for i in range(0,5):         #3
    for j in range(0,5-i):
        print(" ",end=' ')
    for k in range(0,5-i):
        print("*",end=' ')   
    print() 
print("___________________")


for i in range(1,7):            #4
    for j in range(1,7):# i1 j7
        if j>=7-i:
            print("*",end=' ')
        else:   
            print(" ",end=' ') 
    print() 
print("_____________________")  


for i in range(5):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(i+1):
        print(" * ",end=" ")
    print()
print("____________________")
