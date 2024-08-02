import random
tot=0

for i in range(29):
    x=random.randint(0,1)
    tot+=x
nota=(tot/30)*10
print(nota)