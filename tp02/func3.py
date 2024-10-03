from typing import List

def oldmult2(values):
    r = []
    for i in values:
        r.append(i*2)
    
    return r

def mult2(i:int)->int:
    """Multiplie par 2 le truc"""
    return i*2


l =[10,20,30,40,50]
l2 = mult2(l)
print(l2)
l:List =[20,40,60,80,100]

l3 = list(map(mult2,l))
l3 = list(map(lambda i:i*2,l))
print(l3)


