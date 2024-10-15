mytuple =('mayur','adnan','suraj','jhon','waseem')
# mytuple.append("oggy")#cannot add in tupel 
# mytuple.insert(2,"oggy") 

demolist =list(mytuple)
print(type(demolist))
print(type(mytuple))


demolist.append("oggy")
demolist[3] = 'shaikh'
demolist.pop(2)
print(demolist)

mytuple=tuple(demolist)
print(mytuple)