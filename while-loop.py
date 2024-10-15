i = 0
while i<5:
    print('welcome to python progarmming {i}')
    i = i+1
print("____________________")

number = 10 #counting loop
i = 0
while i<number:
    print(i)
    i+=1
print("________________________")

secret_number = 42
guess = 0
while guess !=secret_number:  #guessing game loop 
    guess=int(input("guess a number:"))
    if guess<secret_number:
        print("too low!")
    elif guess>secret_number:
        print("too high!")
print("congratulations! you guessed the number.") 
print("____________________")

#break statement 
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i  += 1
print("____________________")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("____________________")

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
