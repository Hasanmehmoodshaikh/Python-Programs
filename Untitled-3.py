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