print("1. Addition")
print("2. Subtraction")
print("3. multiplication")
print("4. check even or odd")
Choice = int(input("ENTRER YOUR CHOICE -"))

match(Choice):
    case 1:
        a = int(input("ENTER FIRST NUMBER - "))
        b = int(input("ENTER SECOND NUMBER - "))
        print(a+b)
    case 2:
        a = int(input("ENTER FIRST NUMBER - "))
        b = int(input("ENTER SECOND NUMBER - "))
        print(a-b) 
    case 3:
        a = int (input("ENTER FIRST NUMBER - "))
        b = int(input("ENTER SECOND number - "))
        print(a*b)
    case 4:
        num = int(input("ENTER A NUMBER - "))
        if num%2==0:
           print(f'{num} IS A EVEN')
        else:
           print(f'{num} IS A ODD')
    case _:
        print('you enterd a wrong input. please select the option between 1 to 3')