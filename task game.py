import random as r

P1 = "PLAYER1"
P2 = "PLAYER2"
A=0
B=0
 
for round in range(1,4):
    P1 = input("ENTER NAME OF PLAYER 1 - {ADDY} ")
    P2 = input("ENTER NAME OF PLAYER 2 - {COMPUTER} ")
    
    mylist = ['STONE','PAPER','SCISSOR']    
    PLAYER1    = r.choice(mylist)
    PLAYER2    = r.choice(mylist)

    print(f'{P1} - {PLAYER1}')    
    print(f'{P2} - {PLAYER2}')

    if PLAYER1== PLAYER2:
        print("MATCH TIE")
        A=0
        B=0
    elif PLAYER1== 'STONE'   and PLAYER2   == 'SCISSOR':
        print(f"{PLAYER1} WIN")
        ADDY=1
    elif PLAYER1== 'PAPER'   and PLAYER2   == 'STONE':
        print(f"{PLAYER1} WIN")
        ADDY=1
    elif PLAYER1== 'scissro' and PLAYER2   == 'PAPER':
        print(f"{PLAYER1} WIN")
        ADDY=1
        print("YOU WIN THIS ROUND!")
        
        print("___________________")
    else:
        print("PLAYER2 WIN ROUND!")
        COMPUTER=1
    PLAYER1=PLAYER1+"ADDY"
    PLAYER2=PLAYER2+"COMPUTER"

if PLAYER1==PLAYER2:
    print("___________________")
    print(f"{P1} Point is {PLAYER1}")
    print(f"{P2} Point is {PLAYER2}")
    print("_SO MATCH IS TIE")
   
elif PLAYER1> PLAYER2:
    print("___________________")
    print(f"{P1} Point is {PLAYER1}")
    print(f"{P2} Point is {PLAYER2}")
    print("_SO {P1} IS WINSS")
  
else:
    print("_______________")  
    print(f"{P1} Point is {PLAYER1}")
    print(f"{P2} Point is {PLAYER2}")
    print("_SO {P2} IS WINSS") 
        


