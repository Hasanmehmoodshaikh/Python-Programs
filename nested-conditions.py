age = int(input("ENTER YOUR AGE -"))
if age>=18:
    vid = input(" DO YOU HAVE LICENCE ?(Y-YES|N-NO)-")
    if vid =='y':
        print("CONGRATULATIONS! YOU CAN DRIVE.")
    else:
        print("SORRY! YOU CAN NOT DRIVE.")
else:
    print(f"GET LOST! GROW UP AND THEN COME FOR DRIVING AFTER {18-age} YEAR.")    

print("_________________________________")  



age = int(input("ENTER YOUR AGE -"))
if age>=18: 
    vid = input("DO YOU HAVE LICENCE ?(Y-YES|N-NO)-")
    if vid =='y':     
       print("CONGRATULATIONS! YOU CAN DRIVE.")
    else: 
       print("SORRY! YOU CAN NOT DRIVE.") 
else:
    print(f'GET LOST! GROW UP AND THEN COME FOR DRIVING AFTER {18-age} YEAR.')         
