def printnumber(num):
    if num>0:
        print(num)
        printnumber(num-1)
printnumber(5)     
print("_______________________") 


def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))    
print("____________________________")

