def addition():
 n1 = int(input("5 "))             #25
 n2 = int(input("20 "))
r = 5+20
print("Addition is:",r)
print("____________________")

def square(num):                   #16
 return num*num
result=square(4)
print(result)
print(square)
print("________________________")

def division(nr,dr):               #8,33,15
 return nr//dr
d =division(400,50)
print(d)
print(division(100,3))
print(division(75,division(25,5)))
print("________________________")


def max_of_two(x,y):                #16
 if x>y:
  return x
 return y
print(result)
print("_______________________")


def max_of_three(x,y,z):            #6
 return max_of_two(x,max_of_two(y,z))
print(max_of_three(3,6,-5))
print("__________________")

my_string = "python"
x=0
for i in my_string:
 x=x+1
print(my_string[0:x])
for i in my_string:
 x=x-1 
print(my_string[0:x])