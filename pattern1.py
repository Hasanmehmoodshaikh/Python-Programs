for i in range(1,16):
    for j in range(1,i+1):
        print(j,end=' ')
    print() 

print("_________________")

for i in range(1,16):
    for j in range(1,16-i):
        print(j,end=' ')
    print()

print("_____________")

x = 1
for i in range(1,6):
    for j in range(1,6):
       
      
       if x<=9:
        print(f"0{x}",end=" ")
        
       

       else:
        print(x,end=' ')

       x=x+1

    print()