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
print("_____________________________")

x = "y"
YOUR_BALANCE=30000
while x=="y":
   print("1. WITHDERAWL")
   print("2. DEPOSIT")
   print("3. CHECK BALANCE")
   Choice=int(input("ENTER YOUR CHOICE -"))

   match(Choice):
      case 1:
         pin =int(input("ENTER YOU PIN -"))
         if pin ==3897:
            AMOUNT=print(int(input("ENTER YOUR AMOUNT -")))
            A=print("TRANSACTOIN IS COMPELET! PLEASE COLLECT CASH")
         else:
            print("YOU ENTER WRONG PIN TRY AGAIN -")
      case 2:
         pin = int(input("ENTER YOU PIN -"))

         if pin ==3897:
           DEPOSIT=(input("ENTER YOUR DEPOSIT AMOUNT -"))

           print("YOUR DEPOSIT IS COMPELE! DEPOSIT YOUR AMOUNT IN YOUR ACCOUNT ")

         else:
             print("YOU ENTER WRONG PIN TRY AGAIN -")

      case 3:
          pin = int(input("ENTER YOUR PIN -")) 

          if pin ==3897: 
           print(f"YOUR BALACE IS {YOUR_BALANCE}")
    
          else:
           print("YOU ENTER YOU WRONG PIN TRY AGAIN -")

      case _:
        print("SELECT CORRECT CHOICE")
   x=input("DO YOU CONTINUE? (y-YES/n-NO)-")
print("THANKS VISIT AGAIN")
print("_______________________________")

