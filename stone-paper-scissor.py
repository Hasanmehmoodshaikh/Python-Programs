import random as r

a1 = 'adnan1'
m2 = 'mayur2'

mylist = ['ston','paper','scissor']
adnan1 = r.choice(mylist)
mayur2 = r.choice(mylist)

print(f'{a1} - {adnan1}')
print(f'{m2} - {mayur2}')

if a1 == mayur2:
    print("Match tie")
elif a1 == 'stone' and mayur2 =='scissor':
    print(f"{adnan1} Wins")
elif a1 == 'scissor' and mayur2 =='paper':
    print(f"{adnan1} Wins")
elif a1 == 'paper' and mayur2 == 'stone':
    print(f"{adnan1} Wins")
else:
    print(f"{m2} Wins")      