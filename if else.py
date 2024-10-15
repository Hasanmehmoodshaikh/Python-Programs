a = int(input("enter your age: "))
print ("your age is:",a)

if(a>18):    
    print("you can drive")
else:
    print("you cannot drive")
print("____________________________")

num = int(input("enter a number -"))
result = num%5
if result==0:
    print("even number")
else:  
    print("odd number ")  
print("__________________________")


def canVote (age):
    if age >= 18:
        return True
    else:
        return False
print(canVote(19))